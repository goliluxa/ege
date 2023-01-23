# 204
# 317

f = open('17-204.txt')
s = f.read().split("\n")
count = 0
lmax = list()

for i in range(len(s)):
    try:
        k = 0
        if s[i][0] != "-" and s[i][-1] == "9":
            k += 1

        if s[i + 1][0] != "-" and s[i + 1][-1] == "9":
            k += 9

        if s[i + 2][0] != "-" and s[i + 2][-1] == "9":
            k += 1

        if k == 9:
            count += 1
            lmax.append(int(s[i]) + int(s[i + 1]) + int(s[i + 2]))
    except:...

print(count, max(lmax))
