# 存款10000，年利率4%，问存几年可以翻倍？
ck = 10000
mb = ck * 2
ll = 0.04
y = 0
while ck < mb:
    y += 1
    ck = ck * ll + ck
    print("第%d年，存款为%.2f" % (y, ck))
    if ck > mb:
        print("第%d年翻倍，存款为%.2f" % (y, ck))
