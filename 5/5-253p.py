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

    nul = n1.count("0")
    edi = n1.count("1")

    if nul == edi:
        n1 = n1 + n1[-1]
    elif nul < edi:
        n1 = n1 + "0"
    else:
        n1 = n1 + "1"

    nul = n1.count("0")
    edi = n1.count("1")

    if nul == edi:
        n1 = n1 + n1[-1]
    elif nul < edi:
        n1 = n1 + "0"
    else:
        n1 = n1 + "1"

    return int(n1, 2)

l = list()
for i in range(2, 751):
    r = go(i)
    if r % 2 == 0 and r % 4 != 0:
        print(i)

# print(l)
