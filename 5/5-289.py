def funk(n):
    n = list(map(int, list(bin(n)[2:])))
    if n.count(1) % 2 == 0:
        n = [1] + n + [0, 0]
    else:
        n = [1, 1] + n
    s = ""
    for i in n:
       s += str(i)
    return int(s, 2)


for i in range(1, 1000):
    if funk(i) >= 412:
        print(i)
