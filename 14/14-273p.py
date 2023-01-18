#7**2 + 49**4 - 21

s = 7 ** 2 + 49 ** 4 - 21

def base_n(num, base):
    num_base = list()
    while num > 0:
        num_base.append(str(num % base))
        num = num // base
    return num_base[::-1]


print(base_n(s, 14))

