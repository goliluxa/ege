f = open('17-243.txt')
s = f.read().split("\n")
lmax = list()
lNum = list()

for i in s:
    try:
        if int(i) % 19 == 0:
            lNum.append(int(i))
    except:...

maxNum = max(lNum)


for i in range(len(s)):
    try:
        if int(s[i]) > maxNum or int(s[i + 1]) > maxNum:
            lmax.append(int(s[i]) + int(s[i + 1]))
    except:...

print(len(lmax), min(lmax))
