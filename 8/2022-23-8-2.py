from numba import njit


@njit
def sta():
    count = 0
    for i in range(1000000, 10000000000):
        a = i
        n = ''
        k = ''
        while a > 0:
            n = n + str(a % 9)
            a = a // 9
        n = list(n[::-1])
        for j in range(len(n)):
            k += n[j]
        g = str(k)
        if len(g) == 9:
            if g[0] != "2" and g[0] != "4" and g[0] != "6":
                if "7777" not in g:
                    # print(count)
                    count += 1
    if len(g) == 10:
        return count
    return count


print(sta())

# 214962595
