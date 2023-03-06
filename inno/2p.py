from itertools import product


# 0 1 2 3 4 5 6 7 8 9


def go(n):
    l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    l2 = []
    k = 0
    for i in l:
        l2.append([i, k])
        k += 1
    # n = int(input())
    if 8 <= n <= 26:
        for a, b, c, d in product(l2, l2, l2, l2):
            if a[0] + b[0] + c[0] + d[0] == n:
                if ((a[1] <= 2 and b[1] <= 3) or a[1] <= 1) and c[1] < 6:
                    print(f"{a[1]}{b[1]}:{c[1]}{d[1]}")
                    break
    else:
        print("Impossible")


#
# for i in range(7, 24):
#     go(i)
go(int(input()))
