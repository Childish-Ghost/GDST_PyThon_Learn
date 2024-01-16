'''n=67
if n%2==0:
    print("偶数")
else:
    print("奇数")'''

def odd(n):
    if n%2==0:
        return True
    else:
        return False
a=[23,46,55,67,42]
for x in a:
    if odd(x):
        print(x,"是偶数")
    else:
        print(x,"是奇数")

#求n到m之间的和
def qiuhe(n,m):
    s=0
    for i in range(n,m+1):
       s=s+i
    #return s
    print(n,"+",n+1,"+...",m,"=",s)
#print(qiuhe(20,50))
qiuhe(3,333)

def day_income(unit_price,*table_count):
    s=sum(table_count)
    return s*unit_price
dc=[12,9,7,10,7,6,11,9,8,11]
dj=10
print("日营业额是：",day_income(dj,*dc))
print("日营业额是：",day_income(8,1,2,3,4,5,6,7,8,9,10))


def avg(lb):
    return sum(lb)/len(lb)

def avg2(*lb2):
    return sum(lb2)/len(lb2)

print(avg([1,2,3,4,5]))
print(avg2(*[1,2,3,4,5,6]))
      

        
