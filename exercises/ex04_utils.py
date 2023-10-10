"""EX04 - 'list' Utility Functions."""

__author__ = "730578652"


def all(all_list: list[int], parameter2: int) -> bool:
    """Function that returns a bool if the numbers in a list (list1) are the same as the para2."""
    i: int = 0

    if len(all_list) == 0:
        return False

    while len(all_list) > i:
        if parameter2 == all_list[i]:
            i += 1
        else:
            return False
    return True


def max(max_list: list[int]) -> int:
    """Function that returns the largest integer in a list or a ValueError if list is empty."""
    i: int = 0
    alti: int = 1
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    while len(max_list) >= alti:
        if max_list[i] >= max_list[len(max_list) - alti]:
            alti += 1
        else:
            i += 1
            alti = 1
    return max_list[i]


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function that returns True if two lists are the same."""
    if list1 == list2:
        return True
    else:
        return False

