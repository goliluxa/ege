def base_n(num, base):
    num_base = list()
    while num > 0:
        num_base.append(num % base)
        num = num // base
    return num_base


for x in range(100):
    s = 64 ** 11 - 4 ** 10 + 96 - x
    n = base_n(s, 4)
    if sum(n) == 71:
        print(x)
