def func(n):

    summ = sum(map(int, list(str(bin(n))[2:])))

    n = str(bin(n)[2:] + str(summ % 2))

    summ = sum(map(int, list(str(n))))
    n = n + str(summ % 2)
    return int(n, 2)

s1 = list()

for i in range(1, 1000):
    f = func(i)
    if f > 100:
        s1.append(f)

print(min(s1))
