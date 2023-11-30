date={'5102365492':'123456789'}

user=input("请输入你的QQ账号：")

password=input("请输入你的QQ密码：")

if user in date:
    name = date[user]
    if password == name:
        print("1")
    else:
        print("2")
else:
    print("密码错误")