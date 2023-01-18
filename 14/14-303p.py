def base_n(num, base):
    num_base = list()
    while num > 0:
        num_base.append(num % base)
        num = num // base
    return num_base


s = 4 ** 1103 + 3 * 4 ** 1444 - 2 * 4 ** 144 + 66
n = base_n(s, 4)
print(sum(n))
