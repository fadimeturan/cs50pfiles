from numb3rs import validate

def main():
    test_first()
    test_second()

def test_first():
    assert validate(r"5.23.56.9")== True
    assert validate(r"5.56.9")== False
    assert validate(r"5.23.56.88.9")== False

def test_second():
    assert validate(r"5.273.56.9")== False
    assert validate(r"-7.23.56.9")== False
    assert validate(r"5.23.56.9")== True

if __name__ == "__main__":
    main()