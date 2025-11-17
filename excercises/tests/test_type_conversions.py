from exercises.type_conversions import str_to_int, str_to_float, number_to_str, safe_int_conversion

def test_str_to_int():
    assert str_to_int("5") == 5

def test_str_to_float():
    assert abs(str_to_float("3.14") - 3.14) < 1e-9

def test_number_to_str():
    assert number_to_str(123) == "123"

def test_safe_int_conversion():
    assert safe_int_conversion("10") == 10
    assert safe_int_conversion("abc") is None
