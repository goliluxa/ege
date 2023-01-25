s = [str(i) for i in range(1111, 10000)]
lmax = list()

for i in s:
    pr = 1
    sm = 0
    try:
        for j in i:
            pr *= int(j)
            sm += int(j)

        if int(i) % pr == 0 and int(i) % sm == 0:
            lmax.append(int(i))
    except:...

print(len(lmax), max(lmax))
