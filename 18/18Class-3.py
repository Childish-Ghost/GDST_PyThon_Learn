#3、假如你要购买汽车，请输入你的需求找出最佳方案，纯电、混合动力和燃油车，假设车价分别为12万，10万和8万。使用电每100公里10元，使用油每100公里50元，混动以油为主每100公里32元，请根据每年用车公里的需求，算出各种方案的使用成本。

# 单位万元
D_s = 12
H_s = 10
R_s = 8
# 单位每100KM
D_f = 10
H_f = 32
R_f = 50

km = int(input("请输入你的公里数："))

D = km / D_s + D_f / 100
H = km / H_s + H_f / 100
R = km / R_s + R_f / 100

if D == H == R:
    print("三者都可以")
elif D < H < R:
    print("%d公里选购电车会更省钱" % (km))
elif D > H < R:
    print("%d公里选购混动会更省钱" % (km))
elif D > H > R:
    print("%d公里选购燃油会更省钱" % (km))
elif D == H < R:
    print("%d公里选购电动或混动会更同样省钱" % (km))
elif D > H == R:
    print("%d公里选购燃油或混动会更同样省钱" % (km))
elif D == R < H:
    print("%d公里选购燃油或电动会更同样省钱" % (km))
elif D == H > R:
    print("%d公里选购燃油会更同样省钱" % (km))
elif D < H == R:
    print("%d公里选购电车会更同样省钱" % (km))
elif D == R > H:
    print("%d公里选购混动会更同样省钱" % (km))
print(D)
