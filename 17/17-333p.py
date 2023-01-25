f = open('17-333.txt')
s = f.read().split("\n")

lmax = list()
lNum = list()

for i in s:
    if len(i) == 4:
        lNum.append(int(i))

sr = sum(lNum) // len(lNum)


for i in range(len(s)):
    try:
        k = int(s[i]) + int(s[i + 1])

        if str(k) not in s and k < sr:
            sm = 0
            for j in s[i] + s[i + 1]:
                sm += int(j)
            lmax.append(sm)
    except:...

print(len(lmax), max(lmax))
