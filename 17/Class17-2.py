#任务二：冒泡排序
a = [5, 4, 6, 55, 41, 15, 2, 0, 4]


def X_Y(num_list):
    num_len = len(num_list)
    for j in range(num_len):
        for i in range(num_len - 1 - j):#想不明白这两个有什么去吧T_T，这表达式啥意思啊为啥要9-1我能理解但是为啥要减j
                if a[i] < a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]


X_Y(a)
print(a)
'''
a = [5, 4, 6, 55, 41, 15, 2, 0, 4]
num_len = len(a)
for j in range(num_len-1,0,-1):
        for i in range(j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
print(a)

'''