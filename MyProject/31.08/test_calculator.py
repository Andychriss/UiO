from calculator import calculator
import pytest
from math import pi

from pytest import mark
@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]]
    )
    
def test_add():
    assert calculator.add(arg[0], arg[1]) == expected_output

def test_add_decimal():
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)

def test_add_string():
    assert calculator.add("Hello ", "World") == "Hello World"

def test_factorial():
    assert calculator.factorial(5) == (120)

def test_sin():
    assert calculator.sin((2*pi)/4, 6) == pytest.approx(1)

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_multiply():
    assert calculator.multiply(10, 2) == 20

def test_square():
    assert calculator.square(10) == 100

def test_add_string_to_float():
    with pytest.raises(TypeError):
        calculator.add("hello", 3)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
