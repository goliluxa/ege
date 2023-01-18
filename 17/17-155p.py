f = open("17-1.txt", "r")

text = f.read()

l = text.split("\n")
lmin = 0
listmin = list()


for i in range(len(l)):
    try:
        if int(l[i]) > int(l[i + 1]) and int(l[i + 2]) > int(l[i + 1]):
            lmin += 1
            listmin.append(int(l[i + 1]))
    except:
        pass

print(lmin, max(listmin))
