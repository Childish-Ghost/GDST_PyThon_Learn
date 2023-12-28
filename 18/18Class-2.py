import random as r

a = r.randrange(1, 100)
max = 100
min = 1
print(a)
while True:
    x = int(input("x:"))
    if 0 < x < 100:
        if min < x < max:
            if x == a:
                print("恭喜你猜对了")
                break
            elif x < a:
                min = x
                print("范围是%d~%d,请重新输入" % (min, max))
            else:
                max = x
                print("范围是%d~%d,请重新输入" % (min, max))
        else:
            print("范围是%d~%d,请重新输入" % (min, max))
    else:
        print("请正确输入")
