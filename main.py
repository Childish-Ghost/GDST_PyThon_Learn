from Grade_sorting import Grade_sorting
from Grade_Lookup import Grade_Lookup

print("1: 成绩排序", "2: 成绩查找")
num = int(input("请输入排序数值选择："))

if num == 1:
    Grade_sorting()
else:
    if num == 2:
        Grade_Lookup()
