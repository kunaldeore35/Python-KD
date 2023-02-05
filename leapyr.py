lstl = []
lstn = []
for yr in range(2000, 2023):
    if yr % 4==0:
        lstl.append(yr)
    else:
        ans = yr % 4
        yr = yr - ans
        lstn.append(yr)
print(lstl)
print(lstn)