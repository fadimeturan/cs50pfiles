from seasons import check
import pytest

def main():

    test_format()
    test_validity()

def test_format():
    assert check("1234-12-22") == "four hundred fifteen million, one hundred twenty-four thousand, six hundred forty"


def test_validity():
    with pytest.raises(ValueError):
        check("may 11, 1998")

if __name__ == "__main__":
    main()
