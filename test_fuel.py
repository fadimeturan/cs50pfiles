import pytest
from fuel import convert, gauge

def main():
    test_convert_and_gauge()
    test_zero_division()
    test_value()

def test_convert_and_gauge():
    assert convert("1/5") == 20 and gauge(20) == "20%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("may/june")


if __name__ == "__main__":
    main()
