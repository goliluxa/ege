from itertools import product

l = ["W", "B"]

for i in product(l, repeat=20):
    pp = ""
    for j in i:
        pp += j
    print(pp)
