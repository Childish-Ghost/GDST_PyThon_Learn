# 质素
for i in range(100, 0, -1):
    print(i)

# 。。。。
a = [1, 2, 3, 4, 5, 6]
for i in range(len(a)):
    a[i] = a[i] * 10
print(a)

# 乘法表
y = 0
while y < 9:
    y += 1
    for i in range(y, 10):
        print("%d*%d=%d" % (y, i, y * i), end=" ")
    print()

# 排序
import random as r

a = []
for i in range(1, 8):
    a.append(r.randrange(1, 100))
print(a)

for j in range(6, 0, -1):
    for i in range(j):
        if a[i] < a[i + 1]:
            x = a[i]
            a[i] = a[i + 1]
            a[i + 1] = x
    print(a)

#排序 01



# 金字塔
hs = 7
for hh in range(1, 8):
    for i in range(hs - hh):
        print(" ", end="")
    for i in range(hh, 0, -1):
        print(i, end="")
    for i in range(2, hh + 1):
        print(i, end="")
    print()
