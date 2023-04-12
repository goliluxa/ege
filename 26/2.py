import pprint

rad = [list("0" * 100_000)] * 100_000

f = open("26.txt", "r")

n = int(f.readline())
pos = list()
for i in range(n):
    print(i)
    t = [int(x) for x in f.readline()[:-1].split()]
    if t not in pos:
        pos.append(t)


for t in pos:
    # print(i)
    # t = [int(x) for x in f.readline()[:-1].split()]
    rad[t[0] - 1][t[1] - 1] = "1"




for i in rad:
    if k_ch <= 7:
        count += 1
    else:
        count -= k_ch
        if posic[k_pos - 1] < count:
            posic[k_pos - 1] = count
        k_ch = 0
        count = 0
        flag_start = False
    k_pos += 1
    count = 0
    k_ch = 0
    for j in i:
        if j == "1" and not flag_start:
            flag_start = True
            count += 1
            k_ch = 0
            count = 0

        if flag_start:
            if j == "0":
                k_ch += 1
            else:
                k_ch = 0

            if k_ch <= 7:
                count += 1
            else:
                count -= k_ch
                if posic[k_pos - 1] < count:
                    posic[k_pos - 1] = count
                k_ch = 0
                count = 0
                flag_start = False
    print(k_pos)

m = max(posic)
print(m, posic.index(max(posic)))


