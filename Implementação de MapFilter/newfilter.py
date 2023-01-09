def ffilter(f, l):
    if not l:
        return []
    elif f(l[0]):
        return [l[0]] + ffilter(f, l[1:])
    else:
        return ffilter(f, l[1:])