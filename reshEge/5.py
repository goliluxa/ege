def go(n):
    s = [int(n[0]) + int(n[1]), int(n[1]) + int(n[2])]
    s.sort()
    return str(s[0]) + str(s[1])

print(go("843"))
k = 0
for i in range(100, 1000):
    n = go(str(i))
    if n == "1216":
        k += 1
        print(i)

print(k)
