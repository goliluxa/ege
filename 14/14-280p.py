def base_n(num, base):
    num_base = ""
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base


for i in range(2, 11):
    num = base_n(430, i)
    if list(num) == sorted(list(num))[::-1]:
        print(i)
