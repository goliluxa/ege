import itertools


def per(n):
    perm_set = itertools.permutations([1, 2], n)
    l = list()
    k = ''
    print(list(perm_set))
    for i in perm_set:
        for j in i:
            k += str(j)
        l.append(k)
        k = ""
    print(l)



per(3)
