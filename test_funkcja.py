import pytest
from funkcja import jezeli_rok
from funkcja import is_leap_year


@pytest.mark.parametrize('rok', [123, 1231, 2342, 3423, 4323])
def test_rasplpalsxx_aplsldpald(rok):
    assert jezeli_rok(rok) is False


@pytest.mark.parametrize('rok', [64, 2016, 2024, 2020, 4324])
def test_rasplpalsxx_aplsldpaldsa(rok):
    assert jezeli_rok(rok) is True


@pytest.mark.parametrize('year', [2019, 2001, 1967])
def test_years_not_divisible_by_4_are_not_leap_years(year):
    assert is_leap_year(year) is False


@pytest.mark.parametrize('year', [123, 1231, 2342, 3423])
def test_years_not_divisible_by_4_are_not_leap_yearsAA(year):
    assert is_leap_year(year) is False