def printFunc():
    # importation = int(input("输入成绩"))

    raw = [10, 5, 8, 9, 15, 11, 13, 8, 2, 3]

    sort = sorted(raw)

    del sort[0], sort[-1]

    summation = sum(sort) / len(sort)

    print(sort)

    print(summation)
