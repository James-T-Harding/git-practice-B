from ..applications.function import complicated


def test_execute():
    result = complicated("execute arg1 arg2")
    expected = ["arg1", "arg2"]

    assert result == f"Execute with args: {expected}"


def test_count():
    result = complicated("count arg1 arg2")
    assert result == 2


def test_length():
    result = complicated("length string")
    assert result == 6


def test_open():
    result = complicated("open filename")
    assert result == "Open filename"


def test_close():
    result = complicated("close")
    assert result == "Close the program"