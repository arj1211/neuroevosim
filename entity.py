from abc import ABC


class Entity(ABC):
    x: int | float
    y: int | float
    radius: int | float
    color: tuple[int, int, int]
