import pytest
from exercises.number_operations import basic_math_operations, round_and_abs, format_number

def test_basic_math_operations():
    result = basic_math_operations(10, 2)
    assert result["sum"] == 12
    assert result["quotient"] == 5

def test_basic_math_operations_divide_zero():
    with pytest.raises(ValueError):
        basic_math_operations(5, 0)

def test_round_and_abs():
    result = round_and_abs(-12.6789)
    assert result["absolute"] == 12.6789
    assert result["rounded"] == round(-12.6789, 2)

def test_format_number():
    assert format_number(1234.567) == "1,234.57"
