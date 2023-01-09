def fmap(f, l):
    for i, j in enumerate(l):
        l[i] = f(j)