

def odd_or_even(num_a,num_b):
    a=[];b=[];
    for i in range(num_a,num_b):
            if i % 2 ==0:
                a.append(i)

            else:
                b.append(i)

    print('奇数：',a,',偶数',b)
    return '奇数：'+str[a]+',偶数'+str[b]