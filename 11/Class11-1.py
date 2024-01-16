'''
练习：
1、输入个人信息并保存在变量中，然后输出到屏幕上。
包括：学号，姓名，年龄，是否团员，身高
'''

name = input("请输入你的姓名：")
student_ID = input("请输入你的学号：")
ago = input("你的年龄是：")
height = input("你的身高是：")
TY = input("你是否是团员T or F")

if TY == "T" or TY == "t":
    # print(1)
    print("你的学号是%d，你的名字是%d,你的年龄是%d，你是团员，身高%d" % (student_ID, name, ago, height, TY))
elif TY == "F" or TY == "f":
    # print(2)
    print("你的学号是%d，你的名字是%d,你的年龄是%d，你还不是团员，身高%d" % (student_ID, name, ago, height, TY))
else:
    print("参数错误")
