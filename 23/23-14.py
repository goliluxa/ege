def f(x, y, g):
    if x == y:
        return True
    if x > y:
        return False

    return f(x + 1, y, False) + f(x + 2, y, False) + (f(x * 2, y, True) if g == False else 0)


print(f(1, 11, False))
