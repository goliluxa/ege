f = open("files/k7-m2.txt", "r")

a = f.read()
s = list()
s1 = 0
for i in a:
    if i == "C":
        s1 += 1
    else:
        if s1 != 0: s.append(s1)
        s1 = 0
s.append(s1)
print(max(s), len(s), len(a))
