def func(n):
    n = str(bin(n))[2:]
    if n.count("1") > n.count("0"):
        n = n + "0"
    else:
        n = n + "11"

    if n.count("1") > n.count("0"):
        n = n + "0"
    else:
        n = n + "11"

    return int(n, 2)

s1 = list()
for i in range(1, 1000):
    f = func(i)
    if f > 500:
        s1.append(i)
print(min(s1))
