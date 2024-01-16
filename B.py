import random
mb=random.randint(1,100)
min=1
max=100
n=0
while(True):
    print("猜数范围是",min,"~",max,",",end="")
    guess=int(input("请猜数:"))
    n=n+1
    if guess<min or guess>max:
        print("请按指定范围猜数")
        n=n-1
    elif guess==mb:
        print("恭喜你，猜对了！，该数字是:",mb)
        break
    elif guess<mb:
        min=guess+1
    else:
        max=guess-1
print("本次猜数有效次数为：",n,"次")
    
