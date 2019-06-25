from enum import Enum
from typing import TypeVar


class VideoTargetTypes(Enum):
    COLLECTION = 70
    SEASON = 60
    SEQUEL = 60
    VOLUME = 60
    MOVIE = 50
    EPISODE = 50
    CONCERT = 50
    PART = 40
    SESSION = 40
    CHAPTER = 30
    SCENE = 20
    SHOT = 10

    def __repr__(self):
        return "<VideoTargetTypes." + self.name + ": " + self.value + ">\n" + target_type_descriptions[self.value]


class AudioTargetTypes(Enum):
    COLLECTION = 70
    EDITION = 60
    ISSUE = 60
    VOLUME = 60
    OPUS = 60
    ALBUM = 50
    OPERA = 50
    CONCERT = 50
    PART = 40
    SESSION = 40
    TRACK = 30
    SONG = 30
    SUBTRACK = 20
    MOVEMENT = 20

    def __repr__(self):
        return "<AudioTargetTypes." + self.name + ": " + self.value + ">\n" + target_type_descriptions[self.value]


target_type_descriptions = {
    70: "the high hierarchy consisting of many different lower items",
    60: "a list of lower levels grouped together",
    50: "the most common grouping level of music and video (equals to an episode for TV series)",
    40: "when an album or episode has different logical parts",
    30: "the common parts of an album or a movie",
    20: "corresponds to parts of a track for audio (like a movement)",
    10: "the lowest hierarchy found in music or movies"
}
TargetTypes = TypeVar("TargetTypes", VideoTargetTypes, AudioTargetTypes)
TargetTypesInt = TypeVar("TargetTypesInt", VideoTargetTypes, AudioTargetTypes, int)
TargetTypesStr = TypeVar("TargetTypesStr", VideoTargetTypes, AudioTargetTypes, str)