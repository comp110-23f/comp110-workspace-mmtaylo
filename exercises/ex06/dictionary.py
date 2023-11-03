"""EX06 dictionary functions."""

__author__: "730578652"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Function that raises a KeyError if there are more than one of the same keys."""
    key_storage: list[str] = list()
    val_storage: list[str] = list()
    for key in my_dict:
        key_storage += key
        val_storage += my_dict[key]
    my_dict: dict[str, str] = {}
    for i in range(0, len(key_storage)):
        key = val_storage[i]
        my_dict[key] = key_storage[i]
    return my_dict


def favorite_colors(my_dict: dict[str, str]) -> str:
    """Function that returns the color that appears in the dict the most often."""
    color_list: list[str] = my_dict.values()
    color_storage: dict[str, int] = {}
    most_freq_color: str = ''
    max_value: int = 0

    for value in color_list:
        if value in color_storage:
            color_storage[value] += 1
        else:
            color_storage[value] = 1

    for color_storage[value] in color_storage:
        if color_storage[value] > max_value:
            max_value == color_storage[value]
            

    return max_value


def count(my_list: list[str]) -> dict[str, int]:
    """Function that totals the number of each str in a list."""
    storage: dict[str, int] = {}

    for item in my_list:
        if item in storage:
            storage[item] += 1
        else:
            storage[item] = 1

    return storage


def alphabetizer(my_list: list[str]) -> dict[str, list[str]]:
    """"""
    i: int = 0
    letter_storage: list[str] = ()
    my_letter: str = my_list[0]

    while i < len(my_list):
        letter_storage += my_letter[0]
        i += 1

    return letter_storage




def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """"""
    

list = ['cat', 'car', 'apple', 'ant', 'sugar', 'sweet']
x: dict[str, list[str]] = alphabetizer(list)
print(x)