cj = eval(input("请输入成绩："))
if cj >= 90:
    print("成绩等级为A")
elif 80 <= cj < 90:
    print("成绩等级为B")
elif 70 <= cj < 80:
    print("成绩等级为C")
elif 60 <= cj < 70:
    print("成绩等级为D")
elif cj < 60:
    print("成绩等级为E")
    print("不及格请重修")
