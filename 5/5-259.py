def funk(n):
    n = list(map(int, list(bin(n)[2:])))[::-1]
    if 0 in n:
        try:
            n = n[:n.index(0)] + [n[-2], n[-1]] + n[n.index(0) + 1:]
        except:
            pass
    else:
        return 0
    s = ""
    for i in n:
       s += str(i)
    return int(s, 2)

for i in range(10000):
    if funk(i) == 119:
        print(i)
