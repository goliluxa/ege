import time

t = time.time()
f = open('17-346.txt')
s = f.read().split("\n")
count = 0
lmax = list()

for i in range(len(s)):
    try:
        l = s[i] + s[i + 1] + s[i + 2]
        k = 1

        for j in l:
            j1 = int(j)
            if j1 % 2 == 0:
                k *= j1

        if k <= (2 * (10 ** 9)):
            k1 = str(k)
            if (k1[:2]) == "11" and k1.count("6") != 0:
                count += 1
                lmax.append(k)
    except:
        pass

print(count, max(lmax))
print(time.time() - t)




