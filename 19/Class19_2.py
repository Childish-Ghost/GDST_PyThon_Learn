def day_income(unit_price, *table_count):
    zzl = sum(table_count)
    dayxs = zzl * unit_price

    print("%d当日销售菜质量，%d今日营收总额" % (zzl, dayxs))