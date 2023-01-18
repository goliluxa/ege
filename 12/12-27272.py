"""
НАЧАЛО

ПОКА нашлось (111)

    заменить (111, 2)

    заменить (222, 11)

КОНЕЦ ПОКА

КОНЕЦ
"""

def divv(n):
    s = "1" * n

    while "111" in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)

    return s

for i in range(61, 100):
    if divv(i) == "2211":
        print(i)
