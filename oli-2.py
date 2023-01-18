t = int(input())
r = int(input())
l = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())

bal = r * l
if t >= bal:
    print(0)
    exit()

bal -= t
sump = p1 + p2 + p3
x = bal // sump

if bal % sump == 0:
    print(x)
    exit()
c = x * sump
if bal <= c + p1:
    print(x * 3 + 1)
elif bal <= c + p1 + p2:
    print(x * 3 + 2)



