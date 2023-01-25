f = open('17-316.txt')
s = f.read().split("\n")
lmax = list()
summ = sum(sorted([int(i) for i in s[:-1]])[:3])


def prov(n1, n2):
    k = 0
    if n1[0] != n2[0]:
        k += 1

    if n1[1] != n2[1]:
        k += 1

    if n1[2] != n2[2]:
        k += 1

    if n1[3] != n2[3]:
        k += 1
    return k == 2


for i in range(len(s)):
    try:
        cr1 = s[i]
        cr2 = s[i + 1]
        cr3 = s[i + 2]

        if (prov(cr1, cr2) or prov(cr3, cr2) or prov(cr1, cr3)) and int(cr1) + int(cr3) + int(cr2) > summ:
            lmax.append(sum([int(cr1), int(cr2), int(cr3)]))
    except:
        ...

print(len(lmax), max(lmax))
