timeday = {'7:40': '起床', '8：10': '上课', '11：30': '下课', '11：50': '午餐', '12：30': '午睡', '13:40': '起床',
           '14:10': '上课', '17:30': '下课', '18:00': '晚餐', '23:30': '睡觉', }

bb = input("输入你需要查询的时间：")

if bb in timeday:
    print(timeday)
else:
    print("没有对应存库")




fruit = {'苹果': '154', '香梨': '69', '香蕉': '38'}
new_fruit = {'火龙果': '33', '车厘子': '45'}

print(fruit)

fruit['苹果'] = '50'
print("苹果修改", fruit)
print(new_fruit)
new_fruit.pop('车厘子')
print("车厘子修改", new_fruit)

fruit.update(new_fruit)

print(fruit)
print(fruit.values())

nn = input("输入你需要查询的水果名称：")

if nn in fruit:
    print(fruit[nn])
else:
    print("没有对应存库")
