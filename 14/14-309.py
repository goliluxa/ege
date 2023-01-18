def base_n(num, base):
    num_base = list()
    while num > 0:
        num_base.append(num % base)
        num = num // base
    return num_base


s = 103 * 7 ** 103 - 5 * 7 ** 57 + 98
n = base_n(s, 7)
print(sum(n))
