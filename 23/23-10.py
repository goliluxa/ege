def f(x, y):
    if x == y:
        return True
    if x > y:
        return False

    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


print(f(1, 10) * f(10, 12) * f(14, 15))
