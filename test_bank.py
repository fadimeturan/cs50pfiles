from bank import value

def main():
    test_bank()

def test_bank():
    assert value("hohoho") == "$20"
    assert value("lili") == "$100"
    assert value("hello") == "$0"
    assert value("rory") == "$20"


def test_name():
    assert value("HOLLY") == "$20"
    assert value("Hello, Harry") == "$20"


if __name__ == "__main__":
    main()