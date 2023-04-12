def go(n):
    l = sorted(list(str(n).replace("0", "")))
    n1 = int(l[0] + l[1])
    n2 = int(l[-1] + l[-2])
    return n2 - n1

print(go(309))
