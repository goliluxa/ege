def go(n):
    n = str(n)
    if int(n[0]) % 4 == 0:
        n = "9" + n[1:]
        return n
    # elif int(n[0]) % 2:
    #     n = "3" + n[1:]
    return n

k = 0
for i in range(1000, 10000):
    r = go(i)
    if r != "0" and str(oct(int(r)))[-1] == "4":
        k += 1

print(k)
