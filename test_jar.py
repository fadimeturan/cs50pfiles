from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7 )
    assert jar.size == 7
    jar.deposit(3)
    assert jar.size ==10


def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(4)
    assert jar.size == 5