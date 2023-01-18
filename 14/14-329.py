def base_n(num, base):
    num_base = list()
    while num > 0:
        num_base.append(num % base)
        num = num // base
    return num_base


s = 9 ** 81 + 27 ** 729 - 4
s1 = base_n(s, 9)

print(s1.count(max(s1)) + s1.count(0))


