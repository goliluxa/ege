"""
ПОКА нашлось(01) ИЛИ нашлось(02) ИЛИ нашлось(03)
  заменить(01, 30)
  заменить(02, 3103)
  заменить(03, 1201)
КОНЕЦ ПОКА


"""


def divv(ed, dv, tr):
    s = '0' + '1' * ed + '2' * dv + '3' * tr
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '30', 1)
        s = s.replace('02', '3103', 1)
        s = s.replace('03', '1201', 1)
    return s.count('1'), s.count('2'), s.count('3')


for ed in range(1, 60):
    for dv in range(1, 60):
        for tr in range(1, 60):
            s = divv(ed, dv, tr)
            if s[0] == 31 and s[1] == 24 and s[2] == 46:
                print(ed, dv, tr)
                print("stop")
                exit()

