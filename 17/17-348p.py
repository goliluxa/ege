f = open('17-346.txt')
s = f.read().split("\n")
count = 0
lmax = list()

for i in range(len(s)):
    try:
        l = list(s[i]) + list(s[i + 1]) + list(s[i + 2])
        k = 1

        for j in l:
            k *= int(j)
        # print(k)
        if k < (2 * (10 ** 9)):
            k = str(k)
            if (k[0] + k[1]) == "55" and k.count("2") != 0:
                count += 1
                lmax.append(int(k))
    except:
        pass


print(count, max(lmax))

