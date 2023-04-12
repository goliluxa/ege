def go(n):
    n1 = bin(n)[2:]

    nul = n1.count("0")
    edi = n1.count("1")

    if nul == edi:
        n1 = n1 + n1[-1]
    elif nul < edi:
        n1 = n1 + "0"
    else:
        n1 = n1 + "1"

    if len(n1) % 2 == 0:
        n1 = n1[:len(n1) // 2 - 1] + n1[len(n1) // 2 + 1:]
    else:
        n1 = n1[:len(n1) // 2 - 1] + n1[len(n1) // 2 + 1:]

    return int(n1, 2)

k =0
for i in range(2, 1000):
    if go(i) == 58:
        k += 1

print(k)
