def c():
    return a3() * a2()


def a1():
    return 4


def a2():
    return b3() - 2


def a3():
    return a2() + a1()


def b3():
    return a1() * 2


print(c())
