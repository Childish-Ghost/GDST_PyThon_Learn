from Grade_sorting import Grade_sorting
from Grade_Lookup import Grade_Lookup
from Class_or_class import Class_or_class
from Class_dictionary import Class_dictionary
# from chap4_1 import chap4_1

print("1: Grade_sorting", "Grade_Lookup", "3：Class_or_class", "4：Class_dictionary", "5：")
num = int(input("请输入排序数值选择："))

'''
import os

for parent, dirnames, filenames in os.walk('.'):
    # 很多时候需要忽略一些特定目录
    # 忽略 'someenv', '__pycache__', '.idea', '.git', 'venv' 目录
    dirnames[:] = [d for d in dirnames if d not in ['someenv', '__pycache__', '.idea', '.git', 'venv']]
    # 这里完成了对dirnames的筛选，也就是说在接下来的for循环中，
    # someenv和__pycache__将不会被walk
    # 然后，选中所有以".py"结尾的文件
    filenames[:] = [f for f in filenames if f.endswith(".py")]
    for filename in filenames:
        # 输出找到的文件目录
        All_files = os.path.join(parent, filename)
        print(All_files)
'''

if num == 1:
    Grade_sorting()
else:
    if num == 2:
        Grade_Lookup()
    else:
        if num == 3:
            Class_or_class()
        else:
            if num == 4:
                Class_dictionary()
'''         else:
               if num == 5:
                   chap4_1()
                else:
                    print("无内容")
'''