def go(n):
    if n % 2 == 0:
        n1 = n // 2
    else:
        n1 = n - 1

    if n1 % 3 == 0:
        n2 = n // 3
    else:
        n2 = n - 1

    if n2 % 7 == 0:
        n3 = n // 7
    else:
        n3 = n - 1

    return n3


l = list()
for i in range(2, 10000):
    if go(i) == 2:
        l.append(i)

print(len(l))
