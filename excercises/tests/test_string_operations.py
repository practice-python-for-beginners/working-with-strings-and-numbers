from exercises.string_operations import greet_user, count_vowels, reverse_string

def test_greet_user():
    assert "Ada Lovelace" in greet_user("Ada", "Lovelace")

def test_count_vowels():
    assert count_vowels("Python") == 1
    assert count_vowels("aeiouAEIOU") == 10

def test_reverse_string():
    assert reverse_string("abc") == "cba"
