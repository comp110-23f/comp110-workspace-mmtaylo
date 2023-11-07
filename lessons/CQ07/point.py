"""cq07 - intro to object oriented programming challenge."""

from __future__ import annotations

__author__ = "730578652"


class Point:
    """Point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Creating point class."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method to update the x and y attributes."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Mutating method point#scale."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point