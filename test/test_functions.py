"""
Tests for the functions module.
"""

from src.functions import combine

def test_combine():
    expected = "hello world"
    actual = combine("hello ", "world")

    assert expected == actual
