# 1、列出100以内3或7的倍数
x = []
y = []
for i in range(1, 101):
    if i % 3 == 0:
        x.append(i)
    if i % 7 == 0:
        y.append(i)

print("100以内被3整除的数", x)
print("100以内被7整除的数", y)
