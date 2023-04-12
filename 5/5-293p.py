def go(n, m):
    nm = str(n) + str(m)
    p1 = 1
    p2 = 1
    for i in nm:
        if i != "0" and int(i) % 2:
            p1 *= int(i)
        elif i != "0":
            p2 *= int(i)

    return abs(p1 - p2)


for i in range(10000):
    if go(120, i) == 29:
        print(i)
        break

# print(go(256, 108))
