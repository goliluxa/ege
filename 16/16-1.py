def F(n):
    if n < 3:
        return 2
    elif n > 2 and n % 2 == 0:
        return F(n - 2) + F(n - 1) - n
    elif n > 2 and n % 2 != 0:
        return F(n - 1) - F(n - 2) + 2 * n


print(F(32))
