# (x & A ≠ 0)  ( ((x & 17 = 0)  (x & 5 = 0))  (x & 3 ≠ 0) )
l = list()
for A in range(1000000, 100000000):
    if all((x & A != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0) ) for x in range(1000)):
        print(A)
