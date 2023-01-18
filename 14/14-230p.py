def base_n(num, base):
    num_base = ""
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base

for x in range(4, 100):
    s = (88 + 2 * 8 ** x) * 8 ** x + 88 + 8 ** 8
    print(sum(list(map(int, list(base_n(s, 8))))))

