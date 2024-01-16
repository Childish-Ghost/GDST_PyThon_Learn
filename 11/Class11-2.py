'''练习：
2、输入一个3位数整数，输出其百位、十位及个位上的数字。'''
number=int(input("请输入一个三位数："))
c=number%10
a=number//100
b=number%100//10
print(a,b,c)