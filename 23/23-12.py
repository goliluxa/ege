def f(x, y):
    if x == y:
        return True
    if x > y or x == 24:
        return False
    return f(x + 1, y) + f(2 * x + 1, y)


print(f(1, 25))
