from typing import Union

from py_mkv.lib import get_boolean_from_string, noop, get_bool_from_any
from py_mkv.models.codec_id import CodecId
from py_mkv.models.language import Language
from py_mkv.models.tracks.track_id import TrackId, TrackUID
from py_mkv.models.tracks.track_type import TrackType, TrackTypeType


class TrackInfo:
    _track_id: TrackId
    _track_uid: TrackUID
    _type: TrackType
    _is_default: bool
    _lacing: bool
    _minimum_cache: str
    _codec_id: CodecId
    _codec_private_data: str
    _default_duration: str
    _language: Language
    _is_enabled: bool
    _is_forced: bool
    _maximum_block_additional_id: str
    _codec_decode_all: bool
    _name: str

    def __init__(self):
        self.info_mapping_dict = {
            "Track number": self._set_track_id,
            "Track UID": self._set_track_uid,
            "Track type": self._set_type,
            "Default track flag": self._set_is_default,
            "Lacing flag": self._set_lacing,
            "Minimum cache": self._set_minimum_cache,
            "Codec ID": self._set_codec_id,
            "Codec's private data": self._set_codec_private_data,
            "Default duration": self._set_default_duration,
            "Language": self._set_language,
            "Enabled": self._set_is_enabled,
            "Forced track flag": self._set_is_forced,
            "Maximum block additional ID": self._set_maximum_block_additional_id,
            "Codec decode all": self._set_codec_decode_all,
            "Name": self._set_name
        }
        self._track_id = None
        self._track_uid = None
        self._type = None
        self._is_default = False
        self._lacing = False
        self._minimum_cache = None
        self._codec_id = None
        self._codec_private_data = None
        self._default_duration = None
        self._language = Language.English
        self._is_enabled = False
        self._is_forced = False
        self._maximum_block_additional_id = None
        self._codec_decode_all = False
        self._name = None

    def __setitem__(self, key: str, value) -> None:
        if isinstance(value, str):
            value = value.strip(" ")

        if key.startswith("_TrackInfo"):
            key = key[len("_TrackInfo"):]

        self.info_mapping_dict.get(key, noop)(value)

    def __getitem__(self, item):
        return self.info_mapping_dict.get(item, None)

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    @property
    def track_id(self) -> TrackId:
        return self._track_id

    @track_id.setter
    def track_id(self, track_id: Union[str, int, TrackId]) -> None:
        self._set_track_id(track_id)

    def _set_track_id(self, track_id: Union[str, int, TrackId]) -> None:
        if track_id is None:
            self._track_id = None
        elif isinstance(track_id, str):
            self._track_id = TrackId(track_id.strip(" ").split(" ")[0]) - 1
        elif isinstance(track_id, int):
            self._track_id = TrackId(track_id)
        else:
            raise TypeError(f"Type '{type(track_id)}' is not supported for track_id. Expected 'str', 'int', or TrackId")

    @property
    def track_uid(self) -> TrackUID:
        return self._track_uid

    @track_uid.setter
    def track_uid(self, track_uid: Union[str, int, TrackUID]) -> None:
        self._set_track_uid(track_uid)

    def _set_track_uid(self, track_uid: Union[str, int, TrackUID]) -> None:
        if track_uid is None:
            self._track_uid = None
        elif isinstance(track_uid, str):
            self._track_uid = TrackUID(track_uid.strip(" "))
        elif isinstance(track_uid, int):
            self._track_uid = TrackUID(track_uid)
        else:
            raise TypeError("A string, int, or TrackUID must be used when setting the track UID")

    @property
    def type(self) -> TrackType:
        return self._type

    @type.setter
    def type(self, track_type: TrackTypeType) -> None:
        self._set_type(track_type)

    def _set_type(self, track_type: TrackTypeType) -> None:
        if track_type is None:
            self._type = None
        elif isinstance(track_type, str):
            self._type = TrackType.as_track_type(track_type)
        elif isinstance(track_type, TrackType):
            self._type = track_type
        else:
            raise TypeError("A TrackType or string must be used when setting the type")

    @property
    def is_default(self) -> bool:
        if self._is_default is None:
            return False
        else:
            return self._is_default

    @is_default.setter
    def is_default(self, is_default: Union[str, int, bool]) -> None:
        self._set_is_default(is_default)

    def _set_is_default(self, is_default: Union[str, int, bool]) -> None:
        if is_default is None:
            self._is_default = None
        elif isinstance(is_default, str):
            self._is_default = get_bool_from_any(is_default)
        elif isinstance(is_default, bool):
            self._is_default = is_default
        else:
            raise TypeError("A string, int, or boolean must be used when setting the default flag")

    @property
    def lacing(self) -> bool:
        if self._lacing is None:
            return False
        else:
            return self._lacing

    @lacing.setter
    def lacing(self, lacing: Union[str,int, bool]) -> None:
        self._set_lacing(lacing)

    def _set_lacing(self, lacing: Union[str,int, bool]) -> None:
        if lacing is None:
            self._lacing = None
        elif isinstance(lacing, str):
            self._lacing = get_bool_from_any(lacing)
        elif isinstance(lacing, bool):
            self._lacing = lacing
        else:
            raise TypeError("A string, int, or boolean must be used when setting the lacing flag")

    @property
    def minimum_cache(self) -> str:
        return self._minimum_cache

    @minimum_cache.setter
    def minimum_cache(self, minimum_cache: str) -> None:
        self._set_minimum_cache(minimum_cache)

    def _set_minimum_cache(self, minimum_cache: str) -> None:
        if minimum_cache is None:
            self._minimum_cache = None
        elif isinstance(minimum_cache, str):
            self._minimum_cache = minimum_cache
        else:
            raise NotImplemented()

    @property
    def codec_id(self) -> str:
        return self._codec_id

    @codec_id.setter
    def codec_id(self, codec_id: str) -> None:
        self._set_codec_id(codec_id)

    def _set_codec_id(self, codec_id: str) -> None:
        if codec_id is None:
            self._codec_id = None
        elif isinstance(codec_id, str):
            self._codec_id = codec_id
        else:
            raise NotImplemented()

    @property
    def codec_private_data(self) -> str:
        return self._codec_private_data

    @codec_private_data.setter
    def codec_private_data(self, codec_private_data: str) -> None:
        self._set_codec_private_data(codec_private_data)

    def _set_codec_private_data(self, codec_private_data: str) -> None:
        if codec_private_data is None:
            self._codec_private_data = None
        elif isinstance(codec_private_data, str):
            self._codec_private_data = codec_private_data
        else:
            raise NotImplemented()

    @property
    def default_duration(self) -> str:
        return self._default_duration

    @default_duration.setter
    def default_duration(self, default_duration: str) -> None:
        self._set_default_duration(default_duration)

    def _set_default_duration(self, default_duration: str) -> None:
        if default_duration is None:
            self._default_duration = None
        elif isinstance(default_duration, str):
            self._default_duration = default_duration
        else:
            raise NotImplemented()

    @property
    def language(self) -> Language:
        return self._language

    @language.setter
    def language(self, language: Union[str, Language]) -> None:
        self._set_language(language)

    def _set_language(self, language: Union[str, Language]) -> None:
        if language is None:
            self._language = None
        elif isinstance(language, str):
            self._language = Language.value_of(language)
        elif isinstance(language, Language):
            self._language = language
        else:
            raise NotImplemented()

    @property
    def is_enabled(self) -> bool:
        if self._is_enabled is None:
            return False
        else:
            return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled: Union[str, bool]) -> None:
        self._set_is_enabled(is_enabled)

    def _set_is_enabled(self, is_enabled: Union[str, bool]) -> None:
        if is_enabled is None:
            self._is_enabled = None
        elif isinstance(is_enabled, str):
            self._is_enabled = get_boolean_from_string(is_enabled)
        elif isinstance(is_enabled, bool):
            self._is_enabled = is_enabled
        else:
            raise NotImplemented()

    @property
    def is_forced(self) -> bool:
        if self._is_forced is None:
            return False
        else:
            return self._is_forced

    @is_forced.setter
    def is_forced(self, is_forced: Union[str, bool]) -> None:
        self._set_is_forced(is_forced)

    def _set_is_forced(self, is_forced: Union[str, bool]) -> None:
        if is_forced is None:
            self._is_forced = None
        elif isinstance(is_forced, str):
            self._is_forced = get_boolean_from_string(is_forced)
        elif isinstance(is_forced, bool):
            self._is_forced = is_forced
        else:
            raise NotImplemented()

    @property
    def maximum_block_additional_id(self) -> str:
        return self._maximum_block_additional_id

    @maximum_block_additional_id.setter
    def maximum_block_additional_id(self, max_block_additional_id: str) -> None:
        self._set_maximum_block_additional_id(max_block_additional_id)

    def _set_maximum_block_additional_id(self, max_block_additional_id: str) -> None:
        if max_block_additional_id is None:
            self._maximum_block_additional_id = None
        elif isinstance(max_block_additional_id, str):
            self._maximum_block_additional_id = max_block_additional_id
        else:
            raise NotImplemented()

    @property
    def codec_decode_all(self) -> bool:
        if self._codec_decode_all is None:
            return False
        else:
            return self._codec_decode_all

    @codec_decode_all.setter
    def codec_decode_all(self, codec_decode_all: Union[str, bool]) -> None:
        self._set_codec_decode_all(codec_decode_all)

    def _set_codec_decode_all(self, codec_decode_all: Union[str, bool]) -> None:
        if codec_decode_all is None:
            self._codec_decode_all = None
        elif isinstance(codec_decode_all, str):
            self._codec_decode_all = get_boolean_from_string(codec_decode_all)
        elif isinstance(codec_decode_all, bool):
            self._codec_decode_all = codec_decode_all
        else:
            raise NotImplemented()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._set_name(name)

    def _set_name(self, name: str) -> None:
        if name is None:
            self._name = None
        elif isinstance(name, str):
            self._name = name
        else:
            raise NotImplemented()
