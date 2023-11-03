"""Test my zip function."""

__author__ = "730578652"

from lessons.zip import zip


def test_empty_arguments():
    """Testing an empty dict."""
    test_zip: list[str] = list()
    test_zip_2: list[int] = list()
    assert zip(test_zip, test_zip_2) == {}


def test_zip_func():
    """Testing to make sure it works."""
    test_zip: list[str] = ["Hello", "Hi"]
    test_zip_2: list[int] = [2, 3]
    assert zip(test_zip, test_zip_2) == {"Hello": 2, "Hi": 3}


def test_():
    """Testing like values."""
    test_zip: list[str] = ["Hi"]
    test_zip_2: list[int] = [2, 3]
    assert zip(test_zip, test_zip_2) == {}