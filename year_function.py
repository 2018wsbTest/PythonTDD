def year_naw(year=2019):
    leep_year = "podany rok jest rokiem przestępnym"
    normal_year = "podany rok nie jest rokiem przestępnym"
    if year%4==0:
        return leep_year
    else:
        return normal_year


print(year_naw())
print(year_naw(2020))