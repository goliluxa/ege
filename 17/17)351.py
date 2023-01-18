import time

t = time.time()
f = open('17-346.txt')
mas = [int(x) for x in f]
k = 0
maxx = 0
for i in range(2, len(mas)):
    p = 1
    for n in range(3):
        y = str(mas[i - n])
        for x in y:
            if int(x) % 2 == 0:
                p *= int(x)

    if (p <= 2 * 10 ** 9) and (str(p)[:2] == '11') and ('6' in str(p)):
        k += 1
        maxx = max(p, maxx)
print(k, maxx)
# print(time.time() - t)
