def go(n):
    n1 = bin(n)[2:]
    summ = n1.count("1")

    if summ % 2 == 0:
        n1 += "0"
        n1 = "10" + n1[2:]

    elif summ % 2 != 0:
        n1 += "1"
        n1 = "11" + n1[2:]

    return int(n1, 2)


for n in range(2, 100000):
    r = go(n)
    if r > 40:
        print(n)
        break
