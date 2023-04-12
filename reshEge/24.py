with open("24.txt", "r") as f:
    s = f.read()
    k = 0
    l = list()
    for i in s:
        if i == "C":
            k += 1
        else:
            l.append(k)
            k = 0
    l.append(k)

print(max(l))
# print(l)

