import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add_positive(calc):
    assert calc.add(2, 3) == 5

def test_add_negative(calc):
    assert calc.add(-1, -1) == -2

def test_subtract_positive(calc):
    assert calc.subtract(5, 3) == 2

def test_subtract_negative(calc):
    assert calc.subtract(-5, -3) == -2

def test_divide_normal(calc):
    assert calc.divide(10, 2) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
