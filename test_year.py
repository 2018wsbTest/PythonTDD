# import pytest
from year_function import year_naw


def test_2020():
        assert year_naw(2020) == "podany rok jest rokiem przestępnym"
        assert year_naw(2018) == "podany rok nie jest rokiem przestępnym"
        assert year_naw() == "podany rok nie jest rokiem przestępnym"
        assert year_naw(2021) == "podany rok nie jest rokiem przestępnym"
        assert year_naw(2016) == "podany rok jest rokiem przestępnym"

