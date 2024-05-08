import pytest
from working import convert


def main():
    test_convert()
    test_range()
    test_time()
    test_min()
    test_hour()


def test_convert():
    with pytest.raises(ValueError):
        assert convert("8 AM and 9 PM") == ValueError

def test_range():
    with pytest.raises(ValueError):
        assert convert("15 AM to 5 PM") == ValueError

def test_time():
    assert convert("8 AM to 2 PM") == "08:00 to 14:00"

def test_min():
    assert convert("8:44 AM to 9 PM") == "08:44 to 21:00"


def test_hour():
    assert convert("8 AM to 9 PM") == "08:00 to 21:00"

if __name__ == "__main__":
    main()
