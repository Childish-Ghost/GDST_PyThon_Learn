#实训3
fruit1={"苹果":154,"香蕉":38,"香梨":69}
fruit2={"火龙果":33,"车厘子":45}

print(fruit1['苹果'])
#（2）修改苹果数量
fruit1['苹果']=50
print(fruit1['苹果'])
fruit2.pop('车厘子')
print(fruit2)
fruit1.update(fruit2)
print(fruit1)
fruit3=fruit1.copy()
print("各种水果的存库为",fruit3.values())