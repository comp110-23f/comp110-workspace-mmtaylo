"""Combining two lists into a dictionary."""

__author__ = "730578652"


def zip(a_list: list[str], b_list: list[int]) -> dict[str, int]:
    """Function that should produce a dictionary!"""
    a_dictionary: dict[str, int] = {}
    i: int = 0
    if len(a_list) != len(b_list):
        return a_dictionary
    for i in range(len(a_list)):
        a_dictionary[a_list[i]] = b_list[i]
    return a_dictionary