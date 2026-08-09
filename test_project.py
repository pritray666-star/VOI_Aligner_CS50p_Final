# test_project.py — pytest tests for project.py

from project import extract_leading_number, align_voi_data, find_new_entries


def test_extract_leading_number():
    assert extract_leading_number("8_PR") == 8
    assert extract_leading_number("18_adjusYR1_PR") == 18
    assert extract_leading_number(15) == 15
    assert extract_leading_number(15.0) == 15


def test_align_voi_data():
    baseline = [1, 2, 3]
    user_extracted = {
        1: ["1_PR", 100],
        3: ["3_PR", 300],
    }
    aligned_titles, aligned_values, used_numbers = align_voi_data(baseline, user_extracted)

    assert aligned_titles == ["1_PR", "N/V", "3_PR"]
    assert aligned_values == [100, "N/V", 300]
    assert used_numbers == {1, 3}


def test_find_new_entries():
    user_extracted = {
        1: ["1_PR", 100],
        2: ["2_PR", 200],
        5: ["5_PR", 500],
    }
    used_numbers = {1, 2}

    new_titles, new_values = find_new_entries(user_extracted, used_numbers)

    assert new_titles == ["5_PR"]
    assert new_values == [500]