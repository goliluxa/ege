def func(n):
    n2 = ""
    n = list(str(n))
    for i in n:
        n_bin = str(bin(int(i)))[2:]
        n2 += "0" * (4 - len(n_bin)) + n_bin
    n3 = ""
    for i in n2:
        if i == "1":
            n3 += "0"
        else:
            n3 += "1"
    return int(n3, 2)


for i in range(1000):
    try:
        if func(i) == 151:
            print(i)
    except:
        pass
