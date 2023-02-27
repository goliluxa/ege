def f(x, y, g):
    if x == y:
        return True
    if x > y:
        return False
    return f(x + 1, y, g) + f(x + 2, y, g) + (f(x * 2, y, False) if g else 0) + (f(x * 3, y, False) if g else 0)


print(f(1, 11, True))

