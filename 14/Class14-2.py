#第四章的上机实训1
user = 'admin'
password = '1589633'

x = input("请输入你的用户名：")
y = input("请输入你的密码：")

if user == x and y == password:
    print("登录成功")
else:
    print("用户名或密码错误")
