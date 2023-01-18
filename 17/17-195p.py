f = open("17-9.txt", "r")

text = f.read()

l = text.split("\n")
lm = list()
count = 0
for i in range(len(l)):
    k = 0
    try:
        k1 = bin(int(l[i]))
        k2 = bin(int(l[i + 1]))
        k3 = bin(int(l[i + 2]))
        m = max([int(l[i]), int(l[i + 1]), int(l[i + 2])])
        if k1.count("1") >= 3 and k1.count("0") >= 2:
            k += 1
        if k2.count("1") >= 3 and k2.count("0") >= 2:
            k += 1
        if k3.count("1") >= 3 and k3.count("0") >= 2:
            k += 1

        if k >= 2:
            count += 1
            lm.append(m)
            # print(m)
    except:
        pass

print(count, max(lm))
