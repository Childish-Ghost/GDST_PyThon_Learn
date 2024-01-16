#找零钱，找50元零钱，要求20张，面额分别是1,2,及5元的，请输出所有方案
for x in range(0, 21):
    for y in range(0, 21):
        for c in range(0, 11):
            if x + y + c == 20 and x * 1 + y * 2 + c * 5 == 50:
                print("一元%d张，两元%d张,五元%d张" % (x, y, c))
