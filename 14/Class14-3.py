# 输入一个点坐标（x,y），判断其位于哪个象限或坐标轴上
x = int(input("x："))
y = int(input("y："))

if x > 0 and y > 0:
    print("第一象限")
elif x < 0 and y > 0:
    print("第二象限")
elif x < 0 and y < 0:
    print("第三象限")
elif x > 0 and y < 0:
    print("第四象限")
