from plates import is_valid

def main():
    test_char()
    test_alpha()
    test_zero()
    test_punc()


def test_char():
    assert is_valid("hi") == True
    assert is_valid("hello") == True
    assert is_valid("hohohoho") == False

def test_alpha():
    assert is_valid("selam") == True
    assert is_valid("paris") == True
    assert is_valid("italy") == True

def test_zero():
    assert is_valid("my56") == True
    assert is_valid("you08") == False
    assert is_valid("a92") == None

def test_punc():
    assert is_valid("AA23*") == None




if __name__ == "__main__":
    main()

