s = input()
k = int(input())

if k == 0 or s == "":
    print("")
elif k > 0:
    print(s * k)
else:
    print((s[::-1]) * (-k))
