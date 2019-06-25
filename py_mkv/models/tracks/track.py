from typing import NamedTuple, Optional

from py_mkv.lib import get_bool_from_any
from py_mkv.models.codec_id import CodecId
from py_mkv.models.language import Language, LanguageType
from py_mkv.models.offset import Offset, OffsetType
from py_mkv.models.tracks.track_id import TrackId, TrackTypeId, TrackUID
from py_mkv.models.tracks.track_info import TrackInfo
from py_mkv.models.tracks.track_type import TrackType, TrackTypeType


class IdTuple(NamedTuple):
    index: int
    id: TrackId
    uid: TrackUID
    type_id: Optional[TrackTypeId]


class Track:
    __offset: Offset
    __type_id: TrackTypeId
    __info: TrackInfo

    def __init__(self, track_type: TrackTypeType = TrackType.video, track_id: TrackId = TrackId(1), offset: OffsetType = 0, is_default: bool = False, type_id: TrackTypeId = None):
        self.__info = TrackInfo()
        self.type = track_type
        self.offset = offset
        self.track_id = track_id
        self.is_default = is_default
        self.type_id = type_id

    def __repr__(self) -> str:
        return_str = "Track number: " + str(self.track_id)

        if self.__info.track_uid is not None:
            return_str += "\nTrackUID: " + str(self.track_uid)
        if self.__info.type is not None:
            return_str += "\nTrack type: " + str(self.type)
        return_str += "\nDefault track flag: " + str(int(self.__info.is_default))
        return_str += "\nLacing flag: " + str(int(self.__info.lacing))
        if self.__info.minimum_cache is not None:
            return_str += "\nMinimum cache: " + self.__info.minimum_cache
        if self.__info.codec_id is not None:
            return_str += "\nCodec ID: " + self.__info.codec_id
        if self.__info.codec_private_data is not None:
            return_str += "\nCodec's private data: " + self.__info.codec_private_data
        if self.__info.default_duration is not None:
            return_str += "\nDefault duration: " + self.__info.default_duration
        if self.__info.language is not None:
            return_str += "\nLanguage: " + str(self.__info.language)
        return_str += "\nEnabled: " + str(int(self.__info.is_enabled))
        return_str += "\nForced track flag: " + str(int(self.__info.is_forced))
        if self.__info.maximum_block_additional_id is not None:
            return_str += "\nMaximum block additional ID: " + self.__info.maximum_block_additional_id
        return_str += "\nCodec decode all: " + str(int(self.__info.codec_decode_all))
        if self.__info.name is not None:
            return_str += "\nName: " + self.__info.name
        return return_str

    @property
    def type_id(self) -> TrackTypeId:
        return self.__type_id

    @type_id.setter
    def type_id(self, val: TrackTypeId) -> None:
        if val is not None:
            if val.startswith("s") and self.type == TrackType.subtitle:
                self.__type_id = val
            elif val.startswith("a") and self.type == TrackType.audio:
                self.__type_id = val
            elif val.startswith("v") and self.type == TrackType.video:
                self.__type_id = val
            else:
                raise TypeError("type_id: " + val + " is not a valid type id for type: " + self.type.value)
        else:
            self.__type_id = None

    @property
    def offset(self) -> Offset:
        return self.__offset

    @offset.setter
    def offset(self, val: OffsetType) -> None:
        self.__offset = Offset(val)

    @property
    def type(self) -> TrackType:
        return self.__info.type

    @type.setter
    def type(self, val: TrackTypeType) -> None:
        self.__info.type = TrackType.as_track_type(val)

    @property
    def track_id(self) -> TrackId:
        return self.__info.track_id

    @track_id.setter
    def track_id(self, val: TrackId) -> None:
        self.__info.track_id = val

    @property
    def track_uid(self) -> TrackUID:
        return self.__info.track_uid

    @track_uid.setter
    def track_uid(self, val: TrackUID) -> None:
        self.__info.track_uid = val

    @property
    def is_default(self) -> bool:
        return self.__info.is_default

    @is_default.setter
    def is_default(self, val) -> None:
        self.__info.is_default = get_bool_from_any(val)

    @property
    def lacing(self) -> bool:
        return self.__info.lacing

    @lacing.setter
    def lacing(self, val) -> None:
        self.__info.lacing = get_bool_from_any(val)

    @property
    def minimum_cache(self) -> str:
        return self.__info.minimum_cache

    @minimum_cache.setter
    def minimum_cache(self, val) -> None:
        self.__info.minimum_cache = val

    @property
    def codec_id(self) -> CodecId:
        return self.__info.codec_id

    @codec_id.setter
    def codec_id(self, val) -> None:
        self.__info.codec_id = val

    @property
    def codec_private_data(self) -> str:
        return self.__info.codec_private_data

    @codec_private_data.setter
    def codec_private_data(self, val) -> None:
        self.__info.codec_private_data = val

    @property
    def default_duration(self) -> str:
        return self.__info.default_duration

    @default_duration.setter
    def default_duration(self, val) -> None:
        self.__info.default_duration = val

    @property
    def is_enabled(self) -> bool:
        return self.__info.is_enabled

    @is_enabled.setter
    def is_enabled(self, val) -> None:
        self.__info.is_enabled = get_bool_from_any(val)

    @property
    def is_forced(self) -> bool:
        return self.__info.is_forced

    @is_forced.setter
    def is_forced(self, val) -> None:
        self.__info.is_forced = get_bool_from_any(val)

    @property
    def maximum_block_additional_id(self) -> str:
        return self.__info.maximum_block_additional_id

    @maximum_block_additional_id.setter
    def maximum_block_additional_id(self, val) -> None:
        self.__info.maximum_block_additional_id = val

    @property
    def codec_decode_all(self) -> bool:
        return self.__info.codec_decode_all

    @codec_decode_all.setter
    def codec_decode_all(self, val) -> None:
        self.__info.codec_decode_all = get_bool_from_any(val)

    @property
    def name(self) -> str:
        return self.__info.name

    @name.setter
    def name(self, val) -> None:
        self.__info.name = val

    @property
    def language(self) -> Language:
        return self.__info.language

    @language.setter
    def language(self, val: LanguageType) -> None:
        self.__info.language = Language.value_of(val)

    def parse_info_line(self, line: str) -> None:
        line_info_type = line.split("+")[1].split(":")[0].strip(" ")
        line_info_data = ":".join("+".join(line.split("+")[1:]).split(":")[1:])
        self.__info[line_info_type] = line_info_data
