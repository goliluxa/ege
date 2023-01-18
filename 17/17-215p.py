f = open("17-1.txt", "r")

text = f.read()

l = [int(i) for i in text.split("\n")[:-1]]
count = 0
sr = sum(l) / len(l)
lmax = list()

for i in range(len(l)):
    try:
        if max(l[i], l[i + 1]) > sr and (l[i] % 17 == 0 or l[i + 1] % 17 == 0):
            count += 1
            lmax.append(sum([l[i], l[i + 1]]))
    except:
        pass

print(count, max(lmax))
