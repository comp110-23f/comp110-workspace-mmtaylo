"""EX06 dictionary functions."""

__author__ = "730578652"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values in a dict; also raises a KeyError if there are more than one of the same keys."""
    key_storage: list[str] = list()
    val_storage: list[str] = list()

    for key in my_dict:
        key_storage += key
        val_storage += my_dict[key]

    the_dict: dict[str, str] = {}

    for i in range(0, len(key_storage)):
        key = val_storage[i]
        if key in my_dict:
            raise KeyError("This key is already in this dictionary! Try again... ")
        the_dict[key] = key_storage[i]
    
    return the_dict


def favorite_color(my_dict: dict[str, str]) -> str:
    """Function that returns the color that appears in the dict the most often."""
    color_dict: dict[str, int] = {}
    pop_color_frequency: int = 0
    pop_color: str = ""

    for key in my_dict:
        if my_dict[key] in color_dict:
            color_dict[my_dict[key]] += 1
        else:
            color_dict[my_dict[key]] = 1

    for color in color_dict:
        if color_dict[color] > pop_color_frequency:
            pop_color_frequency = color_dict[color]
            pop_color = color

    return pop_color


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
    """Function that takes a dict and produces an alphabetized version in a new dict."""
    my_dict: dict[str, list[str]] = {}

    for item in my_list:
        item = item.lower()
        if item[0] in my_dict:
            my_dict[item[0]].append(item)
        else:
            my_dict[item[0]] = [item]
    
    return my_dict
    

def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Function that updates an attendance roster."""
    if day in attendance:
        attendance[day].append(student)
    else: 
        attendance[day] = [student]
    return attendance