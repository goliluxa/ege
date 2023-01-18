"""
НАЧАЛО

    ПОКА НЕ нашлось (00)

        заменить (01, 210)

        заменить (02, 3101)

        заменить (03, 2012)

    КОНЕЦ ПОКА

КОНЕЦ
"""

def divv(ed, dv, tr):
    s = '0' + '1' * ed + '2' * dv + '3' * tr + "0"
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s.count('1'), s.count('2'), s.count('3')


for ed in range(1, 60):
    for dv in range(1, 60):
        for tr in range(1, 60):
            s = divv(ed, dv, tr)
            if s[0] == 61 and s[1] == 50 and s[2] == 18:
                print(ed + dv + tr + 2)
                print("stop")
                exit()

