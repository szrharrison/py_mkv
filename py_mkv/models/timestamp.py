from datetime import timedelta
from typing import Union, SupportsInt


class Timestamp:
    _duration: timedelta
    _hours: int
    _minutes: int
    _milliseconds: int

    def __init__(self, hours: float = 0, minutes: float = 0, seconds: float = 0, milliseconds: float = 0):
        self._duration = timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
        self._hours = None
        self._minutes = None
        self._milliseconds = None

    def __format__(self, format_spec: str) -> str:
        if format_spec is None or format_spec == "" or format_spec == "r":
            return self.__repr__()
        elif format_spec == "s":
            return self.__str__()
        elif format_spec == "d":
            return f"{self.total_seconds() * 1000:04} ms"
        else:
            raise TypeError("unsupported format spec: " + format_spec + " for class <Timestamp:>")

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}.{self.milliseconds:03d}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.__str__()}>"

    def __add__(self, other: Union[str, bytes, float, SupportsInt, timedelta, 'Timestamp']) -> 'Timestamp':
        if isinstance(other, timedelta):
            result = self._duration + other
        elif isinstance(other, Timestamp):
            result = self._duration + other._duration
        elif isinstance(other, (str, bytes)):
            result = self._duration + Timestamp.from_string(str(other))._duration
        elif isinstance(other, float):
            result = self._duration + timedelta(milliseconds=other)
        else:
            return NotImplemented
        return Timestamp(seconds=result.seconds, milliseconds=int(result.microseconds / 1000))

    @property
    def hours(self) -> int:
        if self._hours is None:
            minutes_remainder = self._duration.seconds % 3_600
            self._hours = int((self._duration.seconds - minutes_remainder) / 3_600)
        return self._hours

    @property
    def minutes(self) -> int:
        if self._minutes is None:
            minutes_remainder = self._duration.seconds % 3_600
            self._minutes = int(minutes_remainder / 60)

        return self._minutes

    @property
    def seconds(self) -> int:
        return self._duration.seconds % 60

    @property
    def milliseconds(self) -> int:
        if self._milliseconds is None:
            self._milliseconds = int(self._duration.microseconds / 1000)

        return self._milliseconds

    def total_seconds(self) -> float:
        return self._duration.total_seconds()

    @staticmethod
    def from_string(string: str) -> 'Timestamp':
        string.strip("'\" ")
        time_parts = string.split(":")
        time_parts = [part.lstrip("0").ljust(1, "0") for part in time_parts]
        seconds = float(time_parts[-1])
        if len(time_parts) == 3:
            return Timestamp(hours=int(time_parts[0]), minutes=int(time_parts[1]), seconds=seconds)
        elif len(time_parts) == 2:
            return Timestamp(minutes=int(time_parts[0]), seconds=seconds)
        elif len(time_parts) == 1:
            return Timestamp(seconds=seconds)
