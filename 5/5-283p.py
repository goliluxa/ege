def go(n):
    n1 = bin(n)[2:]
    # print(n1)
    if n % 2 == 0:
        n1 += bin(n1.count("1"))[2:]
    else:
        n1 = "1" + n1 + "00"
    return int(n1, 2)

for i in range(10000):
    r = go(i)
    if r < 1000:
        print(i)

# go(3)
