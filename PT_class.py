x = eval(input("请输入X轴的坐标："))
y = eval(input("请输入Y轴的坐标："))

if x > 0 and y > 0:
    print("这个坐标位于第一象限")
elif x > 0 > y:
    print("这个坐标位于第四象限")
elif x < 0 < y:
    print("这个坐标位于第二象限")
elif x < 0 and y < 0:
    print("这个坐标位于第三象限")
