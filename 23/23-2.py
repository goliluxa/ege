def f(x, y):
    if x == y:
        return True
    if x > y:
        return False

    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


print(f(3, 9) * f(9, 14))
