def f(x, y):
    if x == y:
        return True
    if x > y or x == 5 or x == 10:
        return False

    return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)


print(f(2, 14))
