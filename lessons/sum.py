"""Summing the elements of a list using different loops."""

__author__ = "730578652"


def w_sum(vals: list[float]) -> float:
    """While loop that returns a sum of all of the items in a list."""
    i: int = 0
    total: float = 0.0
    while i < len(vals):
        total += vals[0 + i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    """For loop that returns a sum of all of the items in a list."""
    total: float = 0.0
    for item in vals:
        total += item
    return total


def f_range_sum(vals: list[float]) -> float:
    """For in range() loop that returns a sum of all of the items in a list."""
    total: float = 0.0
    for item in range(0, len(vals)):
        total += vals[item]
    return total