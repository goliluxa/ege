def base_n(num, base):
    num_base = list()
    while num > 0:
        num_base.append(num % base)
        num = num // base
    return num_base


for x in range(100):
    s = 81**20 - 9**x + 50
    n = base_n(s, 9)
    if sum(n) == 138:
        print(x)
