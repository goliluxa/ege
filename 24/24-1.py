f = open("k7-44.txt", "r")

a = f.read()
s = list()
s1 = 0
for i in a:
    if i == "C":
        s1 += 1
    else:
        s.append(s1)
        s1 = 0
s.append(s1)
print(max(s))

