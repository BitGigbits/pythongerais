def fmap(f, l):
    final = []
    for i in l:
        final.append(f(i))
    l = final
    return l