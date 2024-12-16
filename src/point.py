from typing import Union


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: Union["Point", int]) -> "Point":
        if isinstance(other, self.__class__):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __sub__(self, other: Union["Point", int]) -> "Point":
        if isinstance(other, self.__class__):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

    def __truediv__(self, other: int) -> "Point":
        return Point(self.x / other, self.y / other)

    def __floordiv__(self, other: int) -> "Point":
        return Point(self.x // other, self.y // other)
