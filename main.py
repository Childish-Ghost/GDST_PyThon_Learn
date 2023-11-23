from Grade_sorting import Grade_sorting
from Grade_Lookup import Grade_Lookup
from Class_or_class import Class_or_class
#from Class_gather import Class_gather
from Class_dictionary import Class_dictionary

print("1: 作业_成绩排序并求平均值", "2: 作业_成绩查询", "3：课堂作业_实训4", "4：作业_人员筛选")
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
            # Class_gather()
            else:
                if num == 5:
                    Class_dictionary()
                else:
                    print("无内容")
