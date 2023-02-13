def go(a):
    n = ''
    k = ''
    while a > 0:
        n = n + str(a % 9)
        a = a // 9
    n = list(reversed(n))
    for j in range(len(n)):
        k += n[j]
    return k

count = 0
for i in range(1000000, 10000000000):
    g = str(go(i))
    if len(g) == 9:
        if g[0] not in "246":
            if "7777" not in g:
                print(count)
                count += 1
    if len(g) == 10:
        exit()
print(count)


# 215031680
