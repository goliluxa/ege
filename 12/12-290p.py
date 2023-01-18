"""
ПОКА нашлось (55555)
  заменить (55555, 88)
  заменить (888, 55)
КОНЕЦ ПОКА
"""


def divv(n):
    s = "5" * n
    while "55555" in s:
        s = s.replace("55555", "88", 1)
        s = s.replace("888", "55", 1)
    return s.count("5")


s = list()
for i in range(500):
    n = i + 301
    s.append([divv(n), n])

print(sorted(s))
