from Class19_1 import odd_or_even

a = int(input("最小范围"))
b = int(input("最大范围"))

print(odd_or_even(a, b))

from Class19_5_1 import xf

print(xf(1, 2, 3, 5, 6, 4, 8, 2, 2, 2))

from Class19_2 import day_income

c = 10  # int(input("单价："))

ls = [12, 9, 7, 10, 7, 6, 11, 9, 8, 11]
day_income(c, *ls)
