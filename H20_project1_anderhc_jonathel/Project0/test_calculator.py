from calculator import calculator
import pytest
from math import pi


@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]]
    )
    
def test_add(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize("x, x2", [[(-.1, -.1), -.2], [(.1, .1), .2], [(.1, 0), .1]])
def test_add_decimal(x, x2):
    assert calculator.add(x[0], x[1]) == pytest.approx(x2)


@pytest.mark.parametrize(
    "x, x2", [[("He", "llo"), "Hello"], [("Hello ", "World"), "Hello World"], [("Hey ", "Planet"), "Hey Planet"]])
def test_add_string(x, x2):
    assert calculator.add(x[0], x[1]) == x2

@pytest.mark.parametrize("x, x2", [(1, 1), (2, 2), (3, 6), (5, 120)])
def test_factorial(x, x2):
    assert calculator.factorial(x) == x2


@pytest.mark.parametrize("x, x2", [[(2*pi/4, 6), 1], [(pi/2, 10), 1], [(pi, 15), 0]])
def test_sin(x, x2):
    assert calculator.sin(x[0], x[1]) == pytest.approx(x2)

@pytest.mark.parametrize("x, x2", [[(1, 1), 1], [(4, 2), 2], [(9, 3), 3]])
def test_divide(x, x2):
    assert calculator.divide(x[0], x[1]) == x2


@pytest.mark.parametrize("x, x2", [(0, 0), (1, 1), (2, 4), (3, 9)])
def test_multiply(x, x2):
    assert calculator.multiply(x, x) == x2


@pytest.mark.parametrize("x, x2", [(0, 0), (1, 1), (2, 4), (3, 9)])
def test_square(x, x2):
    assert calculator.square(x) == x2

@pytest.mark.parametrize("x", [("Hello", 3), ("a", 1), ("s", 4), ("b", 9)])
def test_add_string_to_float(x):
    with pytest.raises(TypeError):
        calculator.add(x[0], x[1])


@pytest.mark.parametrize("x", [(0, 0), (1, 0), (2, 0), (3, 0)])
def test_divide_by_zero(x):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(x[0], x[1])
