def base_n(num, base):
    num_base = list()
    while num > 0:
        num_base.append(num % base)
        num = num // base
    return num_base


s = 3 * 11 ** 58 + 15 * 11 ** 55 - 99 * 11 ** 18 + 125 * 11 ** 9 + 381
n = set(base_n(s, 11))
print(len(n))
