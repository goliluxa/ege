
f = open('17-343.txt')
s = f.read().split("\n")
count = 0
lmax = list()

for i in range(len(s)):
    try:
        k = 0

        # Первое число
        a = s[i]
        ss1 = 0  # Доп счётчик
        ss2 = 0  # Доп счётчик

        for j in list(a)[::2]:
            ss1 += int(j)  # Сумма чисел в нечёт поз

        for j in list(a)[1::2]:
            ss2 += int(j)  # Сумма чисел в чёт поз

        if ss1 % ss2 == 0:
            k += 1  # Если усл выполнится

        # Второе число
        a = s[i + 1]
        ss1 = 0  # Доп счётчик
        ss2 = 0  # Доп счётчик

        for j in list(a)[::2]:
            ss1 += int(j)  # Сумма чисел в нечёт поз

        for j in list(a)[1::2]:
            ss2 += int(j)  # Сумма чисел в чёт поз

        if ss1 % ss2 == 0:
            k += 1  # Если усл выполнится

        a = s[i + 2]  # Третье число
        ss1 = 0  # Доп счётчик
        ss2 = 0  # Доп счётчик

        for j in list(a)[::2]:
            ss1 += int(j)  # Сумма чисел в нечёт поз

        for j in list(a)[1::2]:
            ss2 += int(j)  # Сумма чисел в чёт поз

        if ss1 % ss2 == 0:
            k += 1  # Если усл выполнится

        if k == 3:
            count += 1
            lmax.append(sum([int(s[i]), int(s[i + 1]), int(s[i + 2])]))
    except:...


print(count, min(lmax))




