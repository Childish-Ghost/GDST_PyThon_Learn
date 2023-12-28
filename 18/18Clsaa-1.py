for x in range(0, 21):
    for y in range(0, 21):
        for c in range(0, 11):
            if x + y + c == 20 and x * 1 + y * 2 + c * 5 == 50:
                print("一元%d张，两元%d张,五元%d张" % (x, y, c))
