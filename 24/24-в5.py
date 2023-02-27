f = open("files/24_s.txt", "r")

a = f.readlines()
lmax = list()

for i in a:
    lmax.append(i.count("EF"))

k = 0
for i in lmax:
    if i > 1:
        print(i)
        k += 1

print(k)
