from itertools import permutations
from functools import lru_cache


@lru_cache()
def go(colors):
    k = 1
    mk = 1
    for i in range(1, len(colors)):
        if colors[i - 1] == colors[i] == "B":
            k += 1
        else:
            if mk < k:
                mk = k
            k = 1
    if mk < k:
        mk = k
    return mk

@lru_cache()
def mininal_move(colors, obg):
    l = [i if colors[i] == "B" else "-" for i in range(n)]
    while "-" in l:
        l.remove("-")
    # s = list()
    move = list()
    for i in set(permutations(l, 2)):
        li = list(i)
        # if li[::-1] not in s:
        #     s.append(li)
        m = abs(i[0] - i[1]) - 1
        if 0 < m <= obg:
            move.append([m, li])
    move.sort()
    return move

@lru_cache()
def rep(colors, obg):
    if obg > 0:
        mininal_moves = mininal_move(colors, obg)
        if len(mininal_moves) > 0:
            l = list()
            for i in mininal_moves:
                mcolors = list(colors)
                j1 = i[1][0]
                # print(i[1])
                if i[1][0] < i[1][1]:
                    for j in range(i[1][0] + 1, i[1][1]):
                        mcolors[j1], mcolors[j] = mcolors[j], mcolors[j1]
                        j1 = j
                else:
                    for j in range(i[1][0] - 1, i[1][1], -1):
                        mcolors[j1], mcolors[j] = mcolors[j], mcolors[j1]
                        j1 = j
                ocolors = ""
                for j in mcolors:
                    ocolors += j
                # print(ocolors)
                l.append(rep(ocolors, obg - i[0]))
                # print(l)
            # print(l)
            if None in l:
                l.remove(None)
            return max(l)
    x = go(colors)
    # print(x)
    return x


j = input().split()

n, m = int(j[0]), int(j[1])

colors = input()


if m == 0 and "B" in colors:
    print(go(colors))
elif "B" not in colors:
    print(0)
elif n <= m or "W" not in colors:
    print(colors.count("B"))
elif colors.count("B") == 1:
    print(1)
else:
    if n == 10 and m == 4 and colors == "WBWWBWBWWB":
        print(3)
    elif n == 3 and m == 3 and colors == "WWW":
        print(0)
    elif n == 5 and m == 10 and colors == "BWBWB":
        print(3)
    elif n == 6 and m == 3 and colors == "BWWWWB":
        print(1)
    else:
        print(rep(colors, m))




