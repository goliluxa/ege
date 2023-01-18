def base_n(num, base):
    num_base = ""
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base


s = 81**79 + 75**2022 - 12**35
n = base_n(s, 5)
print(n.count("41") + n.count("42") + n.count("43"))
