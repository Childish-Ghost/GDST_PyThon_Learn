#实训4
Python_Course={'张三','李四','王五','赵六','钱七','李雷','韩梅梅'}
C_Course={'赵六','李四','麦克','张三','韩梅梅','李莉','钱七'}

C_Course.add('王五')
Python_Course.remove('王五')

print("选了Python与C语言的同学",Python_Course&C_Course)

print("没有选择C语言的同学",Python_Course-C_Course)

print("共",len(Python_Course)+len(C_Course),"人")