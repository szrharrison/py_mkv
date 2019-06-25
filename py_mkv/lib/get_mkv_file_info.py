import subprocess
from os import PathLike
from pathlib import Path
from typing import List, Union

from py_mkv.lib import esc_file_path
from py_mkv.models.metadata.chapters.chapter import Chapter
from py_mkv.models.mkv import Mkv
from py_mkv.models.timestamp import Timestamp
from py_mkv.models.tracks.track import Track
from py_mkv.models.tracks.track_type import TrackType
from py_mkv.models.tracks.tracks_collection import TracksCollection


def get_mkv_chapters_info(file_info_lines: List[str], duration: Timestamp = None) -> List[Chapter]:
    chapters = []
    reading_chapters = False
    building_chapter = False
    current_chapter_index = 0
    chapters_indentation = 0
    chapter_indentation = 1
    i = 0
    while i < len(file_info_lines):
        line = file_info_lines[i]
        line_prefix = line.split("+")[0]
        indentation = line_prefix.count(" ") + line_prefix.count("|")
        if line.find("Chapters") != -1:
            chapters_indentation = indentation
            reading_chapters = True
            i += 1
        while reading_chapters and i < len(file_info_lines):
            line = file_info_lines[i]
            line_prefix = line.split("+")[0]
            indentation = line_prefix.count(" ") + line_prefix.count("|")
            if indentation <= chapters_indentation:
                reading_chapters = False
                continue

            if line.find("Chapter atom") != -1:
                building_chapter = True
                chapter_indentation = indentation
                chapters.append(Chapter())
                current_chapter_index = len(chapters) - 1
                i += 1

            while building_chapter and i < len(file_info_lines):
                line = file_info_lines[i]
                line_prefix = line.split("+")[0]
                indentation = line_prefix.count(" ") + line_prefix.count("|")
                if indentation <= chapter_indentation:
                    building_chapter = False
                    continue
                else:
                    if line.find(":") != -1:
                        chapters[current_chapter_index].parse_info_line(line)
                    i += 1
        i += 1
    for i, chapter in enumerate(chapters):
        if chapter.end_time is None:
            if i != len(chapters) - 1 and chapters[i + 1].start_time is not None:
                chapter.end_time = chapters[i + 1].start_time
            elif duration is not None:
                chapter.end_time = duration
        if chapter.start_time is None:
            if i == 0:
                chapter.start_time = Timestamp()
            elif chapters[i - 1].end_time is not None:
                chapter.start_time = chapters[i - 1].end_time
    return chapters


def get_mkv_file_info(file_location: Union[str, Path, PathLike]) -> Mkv:
    file_location = esc_file_path(file_location)
    command = "mkvinfo " + file_location
    try:
        file_info_str: str = subprocess.check_output(command, shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output)
    else:
        file_info_lines = file_info_str.split("\n")
        mkv_file = Mkv(file_location)
        mkv_file.tracks = get_mkv_tracks_info(file_info_lines)
        info_indentation = 0
        reading_info = False
        i = 0
        while i < len(file_info_lines):
            line: str = file_info_lines[i]
            line_prefix = line.split("+")[0]
            indentation = line_prefix.count(" ") + line_prefix.count("|")
            if line.find("Segment information") != -1:
                info_indentation = indentation
                reading_info = True
                i += 1
            while reading_info and i < len(file_info_lines):
                line = file_info_lines[i]
                line_prefix = line.split("+")[0]
                indentation = line_prefix.count(" ") + line_prefix.count("|")
                if indentation <= info_indentation:
                    reading_info = False
                    continue
                if line.find("Duration:") != -1:
                    timestamp_string = ":".join(line.split(":")[1:]).strip()
                    mkv_file.duration = Timestamp.from_string(timestamp_string)
                i += 1
            i += 1

        mkv_file.chapters = get_mkv_chapters_info(file_info_lines, mkv_file.duration)

        return mkv_file


def get_mkv_tracks_info(file_info_lines: List[str]) -> TracksCollection:
    tracks = []
    current_track_index = 0
    reading_tracks = False
    building_track = False
    tracks_indentation = 0
    track_indentation = 1
    i = 0
    while i < len(file_info_lines):
        line = file_info_lines[i]
        indentation = line.split("+")[0].count(" ")
        if line.find("Tracks") != -1:
            tracks_indentation = indentation
            reading_tracks = True
            i += 1
        while reading_tracks and i < len(file_info_lines):
            line = file_info_lines[i]
            indentation = line.split("+")[0].count(" ")
            if indentation <= tracks_indentation:
                reading_tracks = False
                continue

            if line.find("Track") != -1:
                building_track = True
                track_indentation = indentation
                tracks.append(Track())
                current_track_index = len(tracks) - 1
                i += 1

            while building_track and i < len(file_info_lines):
                line = file_info_lines[i]
                indentation = line.split("+")[0].count(" ")
                if indentation <= track_indentation:
                    building_track = False
                    continue
                else:
                    if line.find(":") != -1:
                        tracks[current_track_index].parse_info_line(line)
                    i += 1
            track_type = TrackType.as_track_type(tracks[current_track_index].type)
            count_of_type = len(list(filter(lambda track: track.type == track_type, tracks)))
            type_id = track_type.value[0] + str(count_of_type)
            tracks[current_track_index].type_id = type_id
        i += 1

    return TracksCollection(*tracks)
