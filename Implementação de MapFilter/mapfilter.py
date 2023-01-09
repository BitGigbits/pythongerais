def ffilter(f, l):
    if not l:
        return []
    elif f(l[0]):
        return [l[0]] + ffilter(f, l[1:])
    else:
        return ffilter(f, l[1:])

def fmap(f, l):
    final = []
    for i in l:
        final.append(f(i))
    l = final
    return l

new = [2, 4, 7, 11, 3, 12]
result_filter = ffilter(lambda x : x % 2 == 1, new)
fmap(lambda x : x * 3, new)

print(result_filter)
print(new)