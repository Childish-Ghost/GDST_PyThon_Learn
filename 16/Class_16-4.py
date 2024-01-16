x=[]
for num in range(100, 1000):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
                x.append(num)
print(x)