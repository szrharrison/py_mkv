import os
import re
from pathlib import Path
from typing import Union, List, TypeVar, Generic, Callable


def esc_file_path(path: Union[str, Path]):
    return re.sub(r"([ !([\])'\"])", r"\\\1", os.path.normpath(str(path)))


def noop(*args, **kwargs):
    pass


def get_boolean_from_string(val: str) -> bool:
    val = val.strip()
    if val == "1" or val.lower() == "true" or val.lower() == "t":
        return True
    else:
        return False


def get_bool_from_any(val):
    if val is None:
        val = False
    elif isinstance(val, str):
        val = get_boolean_from_string(val)
    elif isinstance(val, bool):
        pass
    elif isinstance(val, float):
        val = val == 1
    else:
        val = False
    return val


T = TypeVar("T")


class IterableInterface(Generic[T]):
    __data__: List[T]
    __curr__: int = 0

    def __init__(self, *args, **kwargs):
        self.__data__ = []

    def __iter__(self):
        return self

    def __next__(self) -> T:
        if self.__curr__ < len(self.__data__):
            self.__curr__ += 1
            return self.__data__[self.__curr__ - 1]
        else:
            self.__curr__ = 0
            raise StopIteration

    def __getitem__(self, item):
        return self.__data__[item]

    def __setitem__(self, key, value):
        self.__data__[key] = value

    def __len__(self):
        return self.__data__.__len__()

    def __sizeof__(self):
        return self.__data__.__sizeof__()


    def find(self, predicate: Callable[[T], bool]) -> T:
        for item in self.__data__:
            if predicate(item):
                return item
            else:
                continue

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return list(filter(predicate, self))


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            if getattr(cls._instances[cls], "__reinit__") is None:
                setattr(cls._instances[cls], "__reinit__", noop)
        cls._instances[cls].__reinit__(*args, **kwargs)
        return cls._instances[cls]
