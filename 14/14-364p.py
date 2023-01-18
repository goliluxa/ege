def n(n, k):
    n = n[::-1]
    g = 0
    for i in range(len(n)):
        g += n[i] * k**i
    return g


ch1 = list("Z YX")
ch2 = list("2X Y")

s = list()
for i in range(10):
    s.append(f"{i}")

s = s + list('abcdefghijklmnopqrstuvwxyz'.upper()) + list('abcdefghijklmnopqrs')



for i in range(len(ch1)):
    if ch1[i] != " ":
        ch1[i] = s.index(ch1[i])

for i in range(len(ch2)):
    if ch2[i] != " ":
        ch2[i] = s.index(ch2[i])


j = list()

for x in range(44):
    ch1[1] = x
    ch2[2] = x
    if (n(ch1, 55) - n(ch2, 55)) % 29 == 0:
        j.append((n(ch1, 55) - n(ch2, 55)))

print(j[1] - j[0])



