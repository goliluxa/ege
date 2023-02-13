def f(x, y):
    if x == y:
        return True
    if x > y:
        return False

    return f(x + 2, y) + f(x * 2, y)


print(f(1, 16) * f(16, 34))
