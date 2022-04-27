from contextlib import AsyncExitStack
from calculator import Calculator

cal = Calculator()


def test_calculator_add():

    assert cal.add(3, 2) == 5


def test_calculator_subtract():
    assert cal.subtract(9, 3) == 6


def test_calculator_multiply():
    assert cal.multiply(2, 5) == 10


def test_calculator_divide():
    assert float(cal.divide(4, 2)) == 2
