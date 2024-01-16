#乘法口诀表
x = 0
while x < 9:
    x += 1
    for i in range(x,10):
        print("%d*%d=%d"%(x,i,i*x),end=' ')
    print()