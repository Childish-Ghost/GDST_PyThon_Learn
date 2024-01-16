# 金字塔
hs = 7
for hh in range(1, 8):
    for i in range(hs - hh):
        print("", end="")
    for i in range(hh, 0, -1):
        print(i, end="")
    for i in range(2, hh + 1):
        print(i, end="")
    print()
