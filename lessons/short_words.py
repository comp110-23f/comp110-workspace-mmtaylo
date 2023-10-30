"""Short Words QZ02 practice."""

__author__ = "730578652"


def short_words(x: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    return_list = []
    for y in x:
        if len(y) > 5:
            return_list.append(y)
        else:
            print(f"{y} is too long!")
    return return_list