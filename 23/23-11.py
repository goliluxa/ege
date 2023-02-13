def f(x, y):
    if x == y:
        return True
    if x > y:
        return False
    return f(x + 2, y) + f(x + 4, y)


print(f(2, 22))
