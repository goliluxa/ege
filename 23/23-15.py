def f(x, y):
    if x == y:
        return True
    if x > y or x == 30:
        return False
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)


print(f(2, 13) * f(13, 39))
