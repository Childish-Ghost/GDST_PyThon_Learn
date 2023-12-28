ck = float(input("你的存款数量："))
cs = ck * 2
y = 0
ll = float(input("利率："))
while ck <= cs:
    ck = ck * ll + ck
    y += 1
    print("第", y, "年，本息", '%.2f' % ck)
    if ck > cs:
        print("第%d年翻倍" % y)
