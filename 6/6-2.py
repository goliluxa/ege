def funk(s1):
    s = s1
    s = (s * 2) // 3
    n = 15
    while s < 4583:
        s = s * 5
        n = n + 7
    return n

k = 2
while True:
    if funk(k) == 43:
        print(k)
    k += 1
