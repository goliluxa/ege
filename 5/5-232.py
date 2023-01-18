def func(n):
    n = str(bin(n))[2:]
    if n.count("1") > n.count("0"):
        n = n + "0"
    else:
        n = n + "1"
    if len(n) % 2 == 0:
        n = n[:len(n) // 2 - 1] + n[len(n) // 2 + 1:]
    else:
        n = n[:len(n) // 2 - 1] + n[len(n) // 2 + 2:]
    return int(n, 2)


for i in range(1000):
    try:
        if func(i) == 55:
            print(i)
    except:
        pass
