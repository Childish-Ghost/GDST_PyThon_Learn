a = [5, 4, 6, 55, 41, 15, 2, 0, 4]
num_len = len(a)
for j in range(num_len-1,0,-1):
        for i in range(j):
            print(i,j)

            if a[i] < a[i + 1]:
                x = a[i]
                a[i] = a[i + 1]
                a[i + 1] = x
print(a)