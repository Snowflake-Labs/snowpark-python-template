from src.udf.functions import combine


def test_combine():
    expected = "hello world"
    actual = combine("hello ", "world")
    assert expected == actual
