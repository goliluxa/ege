def go(n):
    n1 = bin(n)[2:]
    n1 = n1 + n1[-2]
    n1 = n1 + n1[1]
    return int(n1, 2)

for i in range(2, 10000):
    if go(i) > 100:
        print(i)
