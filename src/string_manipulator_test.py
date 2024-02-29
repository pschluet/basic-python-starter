from string_manipulator import duplicate_string


def test_duplicate_string_should_duplicate_string_8_times_when_number_is_8():
    assert duplicate_string(input_str="test", num_repetitions=8) == "test" * 8
