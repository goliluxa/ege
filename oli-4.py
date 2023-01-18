def odin(n, k):
    if n == 1:
        return 0
    x = n // 4
    x = x * k + x
    if n % 2 == 0:
        return x
    else:
        return x + 1



n = int(input())
k = int(input())
s = 0
for i in range(n):
    y = int(input())
    o = odin(y, k)
    s += o if o < y else y - 1
print(s)
