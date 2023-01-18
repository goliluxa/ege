def func(n):
    n = str(bin(n))[2:]
    n = n + n[-2] + n[1]

    return int(n, 2)


s1 = list()

for i in range(2, 1000):
    f = func(i)
    if f > 100:
        s1.append(i)

print(min(s1))
