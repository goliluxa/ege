def delit(num):
    n = 2
    for j in range(2, num // 2 + 1):
        if i % j == 0:
            n += 1
    return n

l = list()
for i in range(568_023, 569_231):
    l.append([delit(i), i])

l.sort()
print(l[::-1])
