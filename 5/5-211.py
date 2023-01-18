def funk(n):
    n = sorted(list(str(n)))
    max_n = n[-1] + n[-2]
    if n[0] == "0":
        return 0
    min_n = n[0] + n[1]
    return int(max_n) - int(min_n)


for i in range(100, 1000):
    if funk(i) == 60:
        print(i)
        break
