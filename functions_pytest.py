from functions import (
    add,
    subtract,
    multiply,
    divide
)

import pytest


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 1, 1),
    (-1, 2, 1),
    (-2, -5, -7),
    (1.5, 2.3, 3.8),
    (5, 2.7, 7.7),
])

def test_add_correct(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,error_type", [
    ("5", 3, TypeError),
    (None, 10, TypeError),
])

def test_add_errors(a, b, error_type):
    with pytest.raises(error_type):
        add(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (0, 1, -1),
    (1, 0, 1),
    (10, 5, 5),
    (-2, 3, -5),
    (5.5, 2.3, 3.2),
    (10, 3.5, 6.5),
])

def test_subtract_correct(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a,b,error_type", [
    ([1], 2, TypeError),
    (7, "2", TypeError),
])

def test_subtract_errors(a, b, error_type):
    with pytest.raises(error_type):
        subtract(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (0, 1, 0),
    (3, 4, 12),
    (-2, 4, -8),
    (-3, -4, 12),
    (2.5, 3, 7.5),
    (1.5, 2.5, 3.75),
])

def test_multiply_correct(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a,b,error_type", [
    ("2", 3, TypeError),
    (4, None, TypeError),
])

def test_multiply_errors(a, b, error_type):
    with pytest.raises(error_type):
        multiply(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (6, 2, 3),
    (0, 5, 0),
    (-10, 2, -5),
    (7.5, 2.5, 3.0),
    (10, 3, 3.3333333333333335),
])

def test_divide_correct(a, b, expected):
    result = divide(a, b)
    
    if isinstance(expected, float) and expected != int(expected):
        assert result == pytest.approx(expected)
    else:
        assert result == expected


@pytest.mark.parametrize("a,b,error_type", [
    (1, 0, ZeroDivisionError),
])

def test_divide_zero_division(a, b, error_type):
    with pytest.raises(error_type):
        divide(a, b)


@pytest.mark.parametrize("a,b,error_type", [
    ("10", 2, TypeError),
    (8, "2", TypeError),
])

def test_divide_type_errors(a, b, error_type):
    with pytest.raises(error_type):
        divide(a, b)