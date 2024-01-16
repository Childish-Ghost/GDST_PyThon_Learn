def xf(*a):
    s=0
    for x in a:
        s= s+x
        return s/len(a)
    print(xf(a))