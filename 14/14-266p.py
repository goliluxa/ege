def base_n(num, base):
    num_base = ""
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base

s = list()
for i in range(2, 11):
    num = base_n(804, i)
    if "1" in num:
        s.append(i)
print(sum(s))

