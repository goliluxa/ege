f = open("17-205.txt", "r")

text = f.read()

l = text.split("\n")
count = 0
lmax = list()

for i in range(len(l)):
    try:
        raz = int(l[i]) - int(l[i + 1])
        if raz % 2 == 0 and raz % 37 == 0:
            count += 1
            lmax.append(int(l[i]) + int(l[i + 1]))
    except:
        pass

print(count, max(lmax))
