# 55x36₁₉ + x2724₁₉
for x in range(0, 19):
    s1 = 5 * 19 ** 4 + 5 * 19 ** 3 + x * 19 ** 2 + 3 * 19 + 6
    s2 = x * 19 ** 4 + 2 * 19 ** 3 + 7 * 19 ** 2 + 2 * 19 + 4
    if (s1 + s2) % 11 == 0:
        print((s1 + s2) // 11)
