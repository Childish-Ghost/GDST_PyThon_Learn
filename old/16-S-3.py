"""
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):  # 创建i数组 数组开始为2，结束为最大值
            if (num % i) == 0:  # 用原始数组除以i数组内的所有数
                break
        else:
            print(num)
"""

mun=23
flag = True
for i in range(2,23):
    if (mun % i)==0:
        flag=False
    break
if flag==True:
    print(0)
else:
    print(1)

