def base_n(num, base):
    num_base = ""
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base

s = list()
for i in range(2, 11):
    num = base_n(1988, i)
    fl = True
    for k in range(10):
        if f"{k}{k}" in num:
            fl = False
    if fl:
        s.append(i)
print(sum(s))

