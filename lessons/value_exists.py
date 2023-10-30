"""Value Exists QZ02 practice."""

__author__ = "730578652"


def value_exists(x: dict[str, int], y: int) -> bool:
    """Function that returns True if argument is in the dict and False if otherwise."""
    exists: bool = False
    for key in x:
        if x[key] == y:
            exists = True
    return exists