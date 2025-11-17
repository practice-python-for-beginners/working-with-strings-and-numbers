#!/usr/bin/env python3
"""
type_conversions.py
GNU GPLv3 License
Covers conversions between strings and numbers.
"""

def str_to_int(value):
    """
    Convert a numeric string to an integer.

    Args:
        value (str)

    Returns:
        int
    """
    return int(value)

def str_to_float(value):
    """Convert a numeric string to a float."""
    return float(value)

def number_to_str(value):
    """Convert a number to its string representation."""
    return str(value)

def safe_int_conversion(value):
    """
    Attempt safe conversion to integer.

    Args:
        value (str)

    Returns:
        int or None
    """
    try:
        return int(value)
    except ValueError:
        return None

if __name__ == "__main__":
    print(str_to_int("42"))
    print(str_to_float("3.14"))
    print(number_to_str(123))
    print("Safe int conversion of 'abc':", safe_int_conversion("abc"))
