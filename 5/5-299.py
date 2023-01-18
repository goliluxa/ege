def funk(n):
    n = list(map(int, list(bin(n)[2:])))
    s_n = sum(n)
    if s_n % 2 == 0:
        n = n[1:]
        for i in n:
            if i == 0:
                n = n[1:]
            if i == 1:
                break
    else:
        n = [1] + n + [0, 0]


    s_n = sum(n)
    if s_n % 2 == 0:
        n = n[1:]
        for i in n:
            if i == 0:
                n = n[1:]
            if i == 1:
                break
    else:
        n = [1] + n + [0, 0]
    s = ""
    for i in n:
       s += str(i)
    return int(s, 2)

for i in range(1, 1000):
    if funk(i) > 100:
        print(i)
