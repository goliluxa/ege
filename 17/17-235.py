f = open('17-1.txt')
s = [int(n) for n in f]
mas = []
srznach = sum(s) / len(s)

for i in range(len(s)):
    try:
        k = 0
        if s[i] > srznach:
            k += 1
        if s[i + 1] > srznach:
            k += 1
        if s[i + 2] > srznach:
            k += 1

        if k >= 2:
            mas.append(s[i] + s[i+1] + s[i+2])
    except:
        pass
print(len(mas), max(mas))
#крч там первый ответ должен быть 5020
