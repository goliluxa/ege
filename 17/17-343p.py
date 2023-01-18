import time

t = time.time()
f = open('17-343.txt')
s = f.read().split("\n")
count = 0
lmax = list()

for i in range(len(s)):
    try:
        k = 0
        a = s[i]
        k += 1 if sum([int(j) for j in list(a)[::2]]) % sum([int(j) for j in list(a)[1::2]]) == 0 else 0
        a2 = s[i + 1]
        k += 1 if sum([int(j) for j in list(a2)[::2]]) % sum([int(j) for j in list(a2)[1::2]]) == 0 else 0
        a3 = s[i + 2]
        k += 1 if sum([int(j) for j in list(a3)[::2]]) % sum([int(j) for j in list(a3)[1::2]]) == 0 else 0

        if k == 3:
            count += 1
            lmax.append(sum([int(a), int(a2), int(a3)]))
    except:
        pass

print(count, min(lmax))
print(time.time() - t)




