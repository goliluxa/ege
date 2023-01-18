"""
НАЧАЛО

    ПОКА нашлось (1111)

        заменить (1111, 22)

        заменить (222, 1)

    КОНЕЦ ПОКА

КОНЕЦ
"""
l = list()
l1 = list()
for i in range(201, 1000):
    s = "1" * i
    while "1111" in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    l1.append(i)
    l.append(len(s))

print(l1[l.index(max(l))])
