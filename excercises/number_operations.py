#!/usr/bin/env python3
"""
number_operations.py
GNU GPLv3 License
Covers arithmetic operations and number formatting.
"""

def basic_math_operations(a, b):
    """
    Perform basic arithmetic operations and return their results.

    Args:
        a (int or float)
        b (int or float)

    Returns:
        dict: Keys - 'sum', 'difference', 'product', 'quotient'
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b
    }

def round_and_abs(value):
    """
    Demonstrate use of abs() and round().

    Args:
        value (float): Input number.

    Returns:
        dict: Rounded and absolute values.
    """
    return {
        "absolute": abs(value),
        "rounded": round(value, 2)
    }

def format_number(num):
    """
    Format number to include commas and two decimal points.

    Args:
        num (float or int)

    Returns:
        str: Formatted number like '1,234.57'
    """
    return f"{num:,.2f}"

if __name__ == "__main__":
    print("Operations:", basic_math_operations(10, 5))
    print("Rounding and abs:", round_and_abs(-12.6789))
    print("Formatted number:", format_number(1234.5678))
  
