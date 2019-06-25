from os import PathLike
from pathlib import Path
from typing import Union, List

from py_mkv.models.metadata.chapters.chapter import Chapter
from py_mkv.models.timestamp import Timestamp
from py_mkv.models.tracks.track_id import TrackId, TrackIdType, TrackTypeId, TrackUID
from py_mkv.models.tracks.track_type import TrackTypeType
from py_mkv.models.tracks.tracks_collection import TracksCollection


class Mkv:
    tracks: TracksCollection
    chapters: List[Chapter]
    duration: Timestamp
    file_path: Path

    def __init__(self, file_location: Union[Path, PathLike, str] = None):
        if isinstance(file_location, Path):
            self.file_path = file_location
        elif isinstance(file_location, str):
            self.file_path = Path(file_location)
        else:
            raise TypeError()
        self.duration = None
        self.tracks = None

    def set_default(self, track_type: TrackTypeType, track_id: TrackIdType) -> None:
        tracks_of_type = self.tracks[track_type]
        if isinstance(track_id, TrackUID):
            for track in tracks_of_type:
                if track.track_uid == track_id:
                    track.is_default = True
                else:
                    track.is_default = False
        elif isinstance(track_id, TrackTypeId):
            number_of_type = self.tracks.count_of_type(track_type)
            index_of_type = track_id.get_index_of_type()
            i = 0
            while i < number_of_type:
                track = tracks_of_type[i]
                if i == index_of_type:
                    track.is_default = True
                    print(str(True))
                    print(str(track.is_default))
                else:
                    track.is_default = False
                i += 1
        elif isinstance(track_id, TrackId):
            for track in tracks_of_type:
                if track.track_id == track_id:
                    track.is_default = True
                else:
                    track.is_default = False
        elif isinstance(track_id, int):
            i = 0
            while i < len(self.tracks):
                track = self.tracks[i]
                if i == (track_id - 1):
                    track.is_default = True
                else:
                    track.is_default = False
                i += 1

    @staticmethod
    def load(path: Union[str, Path, PathLike]) -> 'Mkv':
        from py_mkv.lib.get_mkv_file_info import get_mkv_file_info
        return get_mkv_file_info(path)
