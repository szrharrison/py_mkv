from typing import Union


class TrackId(int):
    def __new__(cls, *args, **kwargs):
        return int.__new__(TrackId, *args, **kwargs)


class TrackUID(int):
    def __new__(cls, *args, **kwargs):
        return int.__new__(TrackUID, *args, **kwargs)


class TrackTypeId(str):
    def __new__(cls, *args, **kwargs):
        return str.__new__(TrackTypeId, *args, **kwargs)

    def get_index_of_type(self) -> int:
        return int(self[1]) - 1


TrackIdType = Union[TrackId, TrackUID, TrackTypeId, int]
