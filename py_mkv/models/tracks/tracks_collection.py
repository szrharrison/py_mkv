from typing import List, Union

from py_mkv.lib import IterableInterface
from py_mkv.models.tracks.track import Track
from py_mkv.models.tracks.track_id import TrackIdType, TrackIdTypeType
from py_mkv.models.tracks.track_type import TrackType, TrackTypeType


class TracksCollection(IterableInterface[Track]):
    __tracks: List[Track]

    def __init__(self, *tracks: Track, **kwargs):
        super().__init__(*tracks, **kwargs)
        if len(tracks) == 0:
            self.__tracks = []
        elif len(tracks) > 0:
            self.__tracks = list(tracks)
        self.__data__ = self.__tracks

    def __getitem__(self, item: Union[TrackTypeType, int]) -> Union[Track, List[Track]]:
        if isinstance(item, (TrackType, str)):
            return self.of_type(item)
        elif isinstance(item, int):
            return self.__tracks[item]
        else:
            raise IndexError()

    def __setitem__(self, key, value):
        raise NotImplemented()

    def __repr__(self) -> str:
        return_string = "<TracksCollection:>:"
        for track in self.__tracks:
            return_string += "\n<Track>:\n" + repr(track)
        return return_string

    def of_type(self, track_type: TrackTypeType) -> List[Track]:
        return [track for track in self.__tracks if track.type == TrackType.as_track_type(track_type)]

    @property
    def video(self) -> List[Track]:
        return self.of_type(TrackType.video)

    @property
    def audio(self) -> List[Track]:
        return self.of_type(TrackType.audio)

    @property
    def subtitles(self) -> List[Track]:
        return self.of_type(TrackType.subtitle)

    def count_of_type(self, track_type: TrackTypeType) -> int:
        return len(self.of_type(track_type))

    def count_of_video(self) -> int:
        return len(self.video)

    def count_of_audio(self) -> int:
        return len(self.audio)

    def count_of_subtitle(self) -> int:
        return len(self.subtitles)

    def get(self, track_id: str, id_type: TrackIdTypeType) -> Track:
        if id_type is TrackIdType.UID:
            return self.find(lambda track: track.track_uid == track_id)
        elif id_type is TrackIdType.NUMBER:
            return self.find(lambda track: track.track_id - 1 == track_id)
        elif id_type is TrackIdType.COUNT:
            return self.find(lambda track: track.track_id == track_id)
        elif id_type is TrackIdType.TYPE_COUNT:
            return self.of_type(track_id[0])[int(track_id[1]) - 1]
        else:
            raise NotImplementedError()
