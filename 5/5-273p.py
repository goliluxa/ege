def go(n):
    n1 = bin(n)[2:]
    # print(n1)
    if n % 2 == 0:
        n1 = "11" + n1 + "11"
    else:
        n1 = "1" + n1 + "0"
    return int(n1, 2)

l = list()
for i in range(10000):
    r = go(i)
    if r < 126:
        l.append(r)

print(max(l))




