from calculator import Calculator


def test_calculator_add():
    cal = Calculator()
    assert cal.add(3, 2) == 5
