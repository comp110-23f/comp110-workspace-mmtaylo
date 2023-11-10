"""cq07 - intro to object oriented programming challenge."""

from __future__ import annotations

__author__ = "730578652"


class Point:
    """Point class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
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
    
    def __str__(self) -> str:
        """0: __str__ - magic method that prints out points in a readable way."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """1: __mul__ - magic method to overload the multiplication operator."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __add__(self, factor: int | float) -> Point:
        """2: __ad__ - magic mwthod to overload the addition operator."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point