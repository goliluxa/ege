f = open("files/24_s.txt", "r")

a = f.readlines()
lmax = list()

for i in a:
    lmax.append(i.count("EF"))

print(max(lmax))


# print(lmax)
