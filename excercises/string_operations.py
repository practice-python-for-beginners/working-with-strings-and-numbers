#!/usr/bin/env python3
"""
string_operations.py
GNU GPLv3 License
Demonstrates string manipulation and formatting.
"""

def greet_user(first_name, last_name):
    """
    Create a greeting message using f-string formatting.

    Args:
        first_name (str): User's first name.
        last_name (str): User's last name.

    Returns:
        str: Personalized greeting message.
    """
    return f"Hello, {first_name} {last_name}! Welcome to Python."

def count_vowels(text):
    """
    Count the number of vowels in a given string (case-insensitive).

    Args:
        text (str): Input string.

    Returns:
        int: Number of vowels.
    """
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

def reverse_string(text):
    """Return the reverse of the provided string."""
    return text[::-1]

if __name__ == "__main__":
    sample = "Python"
    print(greet_user("Ada", "Lovelace"))
    print(f"Vowel count in '{sample}':", count_vowels(sample))
    print("Reversed:", reverse_string(sample))
  
