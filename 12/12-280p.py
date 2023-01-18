"""
ПОКА нашлось (555) ИЛИ нашлось (888)
  заменить (555, 8)
  заменить (888, 55)
КОНЕЦ ПОКА
"""

def divv(n):
    s = "5" * n
    while "555" in s or "888" in s:
        s = s.replace("555", "8", 1)
        s = s.replace("888", "55", 1)
    return s

s = list()
for i in range(500):
    n = i + 301
    r = divv(n)
    if r.count("8") == 1 and r.count("5") == 1:
        s.append(n)

print(sorted(s)[0])


