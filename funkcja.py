def jezeli_rok(rok: int) -> bool:
    return bool(not rok % 4 and rok % 100 or not rok % 400)


def is_leap_year(year: int) -> bool:
    return bool(not year % 4 and year % 100 or not year % 400)