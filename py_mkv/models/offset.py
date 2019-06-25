from typing import Union


class Offset:
    value: float

    def __init__(self, value: 'OffsetType'):
        self.value = Offset.__get_other_as_number(value)

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    def __ne__(self, other) -> bool:
        return str(self) != str(other)

    def __truediv__(self, other: 'OffsetType') -> 'Offset':
        return Offset(self.value / Offset.__get_other_as_number(other))

    def __floordiv__(self, other: 'OffsetType') -> 'Offset':
        return Offset(self.value // Offset.__get_other_as_number(other))

    def __mul__(self, other: 'OffsetType') -> 'Offset':
        return Offset(self.value * Offset.__get_other_as_number(other))

    def __add__(self, other: 'OffsetType') -> 'Offset':
        return Offset(self.value + Offset.__get_other_as_number(other))

    def __radd__(self, other: 'OffsetType') -> 'Offset':
        return Offset(self.value + Offset.__get_other_as_number(other))

    @staticmethod
    def __get_other_as_number(other: 'OffsetType') -> float:
        if isinstance(other, Offset):
            return other.value
        elif isinstance(other, str):
            return float(other)
        elif isinstance(other, (int, float)):
            return other
        else:
            raise NotImplemented


OffsetType = Union[float, int, str, 'Offset']
