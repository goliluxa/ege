def f(x, y):
    if x == y:
        return True
    if x < y:
        return False
    return f(minus(x), y) + f(obnul(x), y)


def minus(n):
    n = int(str(n), 2)
    n -= 1
    n = bin(n)[2:]
    return int(n)

def obnul(n):
    s = "1" + "0" * (len(str(n)) - 1)
    if s == str(n):
        return 0
    return int(s)


print(f(1000000, 1000))


