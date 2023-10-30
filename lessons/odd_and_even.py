"""Odd and Even QZ02 Practice."""

__author__ = "730578652"

def odd_and_even(my_list: list[int]) -> list[int]:
    """"""
    i: int = 0
    return_list: list[int] = []

    while i < len(my_list):
        if my_list[i] != 0 and i % 2 == 0:
            return_list.append(my_list[i])
        i += 1

    return return_list
