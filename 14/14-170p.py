def base_n(num, base):
    num_base = ""
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base


s = 9 ** 7 - 3 ** 12 + 3 ** 21 - 19
print(s)
print(base_n(s, 3).count("2"))
