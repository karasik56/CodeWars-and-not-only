from test_func import division
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(10, 5, 2), (20, 2, 10), (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10,0)