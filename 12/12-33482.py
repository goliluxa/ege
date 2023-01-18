l = list()
l1 = list()
for i in range(101, 1000):
    s = "1" * i
    while "111" in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    print(i, s.count("1"))


