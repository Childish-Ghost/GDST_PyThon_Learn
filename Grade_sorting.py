# importation = int(input("输入成绩"))
def Grade_sorting():
    raw = [10, 5, 8, 9, 15, 11, 13, 8, 2, 3]

    sort = sorted(raw)  # sorted 顺序排序 小→大 ；括号内是数组，元组

    del sort[0], sort[-1]

    summation = sum(sort) / len(sort)

    print(sort)

    print(summation)
    print("2023/11/16")
