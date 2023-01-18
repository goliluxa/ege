def funk(n):
    n = list(map(int, list(str(n))))
    s1 = 0
    s2 = 0
    for i in range(len(n)):
        if n[i] % 2 != 0:
            s1 += n[i]
        if (i + 1) % 2 == 0:
            s2 += n[i]

    return abs(s1 - s2)

for i in range(1000000000):
    n = funk(i)
    if n == 29:
        print(i)
        break



