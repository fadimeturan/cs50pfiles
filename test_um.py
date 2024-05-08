import pytest
from um import count

def main():
    test_counter()
    test_char()
    test_space()
    
def test_counter():
    assert count("um um yummy") == 2
    assert count("hi, um") == 1

def test_char():
    assert count("hey, um?") == 1

def test_space():
    assert count("yum um mum um") == 2

if __name__ == "__main__":
    main()