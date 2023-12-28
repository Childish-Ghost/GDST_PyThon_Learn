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
print(D)
