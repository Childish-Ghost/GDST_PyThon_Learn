date = {'5102365492': '123456789', '562248522': '2256524561'}

user = input("请输入你的QQ账号：")

password = input("请输入你的QQ密码：")

if user in date:
    name = date[user]
    if password == name:
        print("欢迎使用")
    else:
        print("密码错误")
else:
    print("密码错误")
