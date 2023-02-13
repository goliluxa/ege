def go(n):
    d_n = bin(n)[2:]
    d_n = d_n[:-1]
    # print(d_n)
    if n % 2 == 0:
        d_n += "10"
    else:
        d_n += "01"
    return int(d_n, 2)


for i in range(2, 100000):
    if go(i) == 2018:
        print(i)

