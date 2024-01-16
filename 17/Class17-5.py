import random

x = []
for i in range(0, 10):
    x.append(random.randrange(0, 101))
print(x)

y = len(x)
for i in range(y - 1, 0, -1):
    for j in range(i):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
print(x)
