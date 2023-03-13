def funk(s1):
    s = s1
    s = (s * 2) // 7
    n = 15
    while s < 5000:
        s = s * 5
        n = n + 7
    print(n, s1)
    return n

k = 4
while True:
    if funk(k) == 50:
        print(k)
        break
    k += 1
