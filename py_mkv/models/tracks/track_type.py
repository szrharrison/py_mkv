from enum import Enum
from typing import Union, Iterable

VIDEO = "video"
AUDIO = "audio"
SUBTITLE = "subtitle"
BUTTON = "button"


class TrackType(Enum):
    video = VIDEO
    vid = VIDEO
    v = VIDEO
    audio = AUDIO
    aud = AUDIO
    a = AUDIO
    subtitle = SUBTITLE
    subtitles = SUBTITLE
    subs = SUBTITLE
    sub = SUBTITLE
    s = SUBTITLE
    button = BUTTON
    b = BUTTON

    def __repr__(self) -> str:
        return '<' + self.__class__.__name__ + '.' + self.name + '>'

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other: 'TrackTypeType') -> bool:
        if isinstance(other, TrackType):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == TrackType.as_track_type(other).value
        else:
            return NotImplemented

    @staticmethod
    def as_track_type(val: 'TrackTypeType') -> 'TrackType':
        if isinstance(val, TrackType):
            return val
        elif isinstance(val, str):
            val = val.strip(" ")
            return TrackType[val]
        else:
            raise TypeError()


TrackType.types: Iterable[TrackType] = [
    TrackType.video,
    TrackType.vid,
    TrackType.v,
    TrackType.audio,
    TrackType.aud,
    TrackType.a,
    TrackType.subtitle,
    TrackType.subtitles,
    TrackType.subs,
    TrackType.sub,
    TrackType.s,
    TrackType.button,
    TrackType.b
]

TrackTypeType = Union[TrackType, str]
