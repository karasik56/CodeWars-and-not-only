from create_phone_number import create_phone_number
import pytest

# [([0, 2, 3, 0, 5, 6, 0, 8, 9, 0], "(023) 056-0890"))]


@pytest.mark.parametrize('n, expected_result', [([0, 2, 3, 0, 5, 6, 0, 8, 9, 0], "(023) 056-0890"), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890")])
def test_correct_phone_number(n, expected_result):
    assert create_phone_number(n) == expected_result

