f = open('17-353.txt')
s = f.read().split("\n")[:-1]

s1 = [int(i) for i in s]
sr = (max(s1) + min(s1)) // 2

lmax = list()

for i in range(len(s) // 2 - 1):
    # print(s1[i], s1[- i - 1])
    k = 0
    if s1[i] > sr > s1[- i - 1]:
        k += 1
    if s1[i] < sr < s1[- i - 1]:
        k += 1

    if k == 1:
        lmax.append(s1[i] + s1[- i - 1])

print(len(lmax), max(lmax))



