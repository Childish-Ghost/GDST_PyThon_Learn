'''xh=input("请输入您的学号：")
nl=int(input("请输入年龄："))
tz=float(input("体重:"))
print("学号：",xh,",年龄：",nl)'''
yz=(1,2,3,4,5)
print(yz,yz[-2])
print(yz[1:3])
lb=[1,2,3,4,5]
lb.append(6)
lb.pop(0)
print(lb[-1])
print(lb)
zd={"A":1,"B:":2}
print(zd)
zd["C"]=3
print(zd)
print(zd.keys())
jh={1,2,3}
print(jh)
jh2={3,4}
print(jh2&jh)
print(jh2|jh)
print(jh2-jh)
print(jh-jh2)
print(jh^jh2)

import random
guessaim=random.randint(1,100)
print(guessaim)

a=[]
for i in range(10):
    a.append(random.randint(1,100))
print(a)
b=[9,8,7,6,5,4]
for x in b:
    if x %2==0:
        print(x,"是偶数")
for i in range(len(b)):
    b[i]=b[i]*5
print(b)
