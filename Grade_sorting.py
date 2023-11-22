raw = [10, 5, 8, 9, 15, 11, 13, 8, 2, 3]

sort = sorted(raw)

del sort[0], sort[-1]

summation = sum(sort)/8
print(sort)
print(summation)