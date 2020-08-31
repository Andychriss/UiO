from calculator import calculator
import pytest
from math import pi

def test_add():
    assert calculator.add(1, 2) == 3

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
    assert calculator.square(10, 2) == 100