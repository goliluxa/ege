def f(x, y):
    if x == y:
        return True
    if x > y:
        return False
    return f(x + 1, y) + f(x * 2, y)


print(f(1, 16))
