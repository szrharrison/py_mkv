from enum import Enum
from typing import Union


class AudioFileExtension(Enum):
    AAC = ".aac"
    AC3 = ".ac3"
    CAF = ".caf"
    DTS = ".dts"
    FLAC = ".flac"
    MP2 = ".mp2"
    MP3 = ".mp3"
    OPUS = ".opus"
    WAV = ".wav"
    RM = ".rm"
    REAL_MEDIA = ".rm"
    RMVB = ".rmvb"
    REAL_MEDIA_VARIABLE_BITRATE = ".rmvb"
    MLP = ".mlp"
    TRUE_HD = ".thd"
    THD = ".thd"
    TRUE_AUDIO = ".tta"
    TTA = ".tta"
    OGG = ".ogg"
    VORBIS = ".ogg"
    WAV_PACK = ".wv"
    WV = ".wv"


class SubtitleFileExtension(Enum):
    PGS = ".sup"
    SUBTITLE_BITMAP = ".sup"
    SUP = ".sup"
    KATE = ".ogx"
    OGX = ".ogx"
    SSA = ".ssa"
    ASS = ".ass"
    SRT = ".srt"
    SUB = ".sub"
    IDX = ".idx"
    USF = ".usf"
    UNIVERSAL_SUBTITLE_FORMATTING = ".usf"
    WEB_VTT = ".vtt"


FileExtension = Union[AudioFileExtension, SubtitleFileExtension]
