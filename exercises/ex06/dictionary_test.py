"""Testing my dictionary functions."""

__author__ = "730578652"
import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_empty_arguments() -> None:
    """Invert test 1: with no arguments, this function should produce an empty dict."""
    test_invert: dict[str, str] = {}
    assert invert(test_invert) == {}


def test_invert_KeyError() -> None:
    """Invert test 2: making sure that a KeyError is raised."""
    with pytest.raises(KeyError):
        invert({"a": "b", "c": "b"})


def test_invert_correctly_inverting_multiple_pairs() -> None:
    """Invert test 3: making sure that keys and values are properly inveritng/switiching places."""
    test_invert: dict[str, str] = {"apple": "banana", "crab": "dim", "egg": "fish", "great": "hi", "igloo": "jest"}
    assert invert(test_invert) == {"banana": "apple", "dim": "crab", "fish": "egg", "hi": "great", "jest": "igloo"}


def test_favorite_color_empty_arguments() -> None:
    """Favorite_color test 1: if the arguments are empty, then no str should be produced."""
    test_favorite_color: dict[str, str] = {}
    assert favorite_color(test_favorite_color) == ''


def test_favorite_color_correct_return() -> None:
    """Favorite_color test 2: making sure the correct str is returned."""
    test_favorite_color: dict[str, str] = {"caroline": "purple"}
    assert favorite_color(test_favorite_color) == "purple"


def test_favorite_color_correct_popular_color_return() -> None:
    """Favorite_color test 3: making sure the most popular color in the argument list is returned."""
    test_favorite_color: dict[str, str] = {"caroline": "purple", "daniel": "green", "haley": "orange", "carter": "green"}
    assert favorite_color(test_favorite_color) == "green"


def test_count_empty_arguments() -> None:
    """Count test 1: if the arguments are empty, then the returned dict should also be empty."""
    test_count: list[str] = []
    assert count(test_count) == {}


def test_count_correct_return() -> None:
    """Count test 2: making sure the function returns a proper dictionary."""
    test_count: list[str] = ["a", "a"]
    assert count(test_count) == {"a": 2}


def test_count_correctly_counting() -> None:
    """Count test 3: making sure each item in the list is properly counted."""
    test_count: list[str] = ["a", "b", "c", "a", "a", "c"]
    assert count(test_count) == {"a": 3, "b": 1, "c": 2}


def test_alphabetizer_empty_arguments() -> None:
    """Alphabetizer test 1: if the argument list is empty, then an empty dict should be produced."""
    test_alphabetizer: list[str] = []
    assert alphabetizer(test_alphabetizer) == {}


def test_alphabetizer_correct_return() -> None:
    """Alphabetizer test 2: making sure the function returns a proper dictionary."""
    test_alphabetizer: list[str] = ["cat"]
    assert alphabetizer(test_alphabetizer) == {"c": ["cat"]}


def test_alphabetizer_correct_alphabetizing() -> None:
    """Alphabetizer test 3: making sure each item in the list is properly sorted according to their first characters."""
    test_alphabetizer: list[str] = ["cat", "dog", "fish", "Cow", "Deer"]
    assert alphabetizer(test_alphabetizer) == {"c": ["cat", "Cow"], "d": ["dog", "Deer"], "f": ["fish"]}


def test_update_attendance_() -> None:
    """Update_attendance test 1: ."""
    test_update_attendance_0: dict[str, list[str]] = {"monday": ["a", "b"]}
    test_update_attendance_1: str = "monday"
    test_update_attendance_2: str = "a"
    assert update_attendance(test_update_attendance_0, test_update_attendance_1, test_update_attendance_2) == {"monday": ["a", "b"]}


def test_update_attendance_new_day_and_student_attendance() -> None:
    """Update_attendance test 2: adding a new day to the dict with new attendance record."""
    test_update_attendance_0: dict[str, list[str]] = {"monday": ["a", "b"], "tuesday": ["b", "c"]}
    test_update_attendance_1: str = "wednesday"
    test_update_attendance_2: str = "b"
    assert update_attendance(test_update_attendance_0, test_update_attendance_1, test_update_attendance_2) == {"monday": ["a", "b"], "tuesday": ["b", "c"], "wednesday": ["b"]}


def test_update_attendance_existing_day_adding_new_student_attendane() -> None:
    """Update_attendance test 3: adding a student to an already existing day in the dict."""
    test_update_attendance_0: dict[str, list[str]] = {"monday": ["a", "b"], "tuesday": ["b", "c"], "wednesday": ["a", "b", "c"]}
    test_update_attendance_1: str = "monday"
    test_update_attendance_2: str = "c"
    assert update_attendance(test_update_attendance_0, test_update_attendance_1, test_update_attendance_2) == {"monday": ["a", "b", "c"], "tuesday": ["b", "c"], "wednesday": ["a", "b", "c"]}