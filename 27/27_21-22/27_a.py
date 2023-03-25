import pprint
from itertools import product

def funk(l):
    if len(l) == 1:
        return l
    else:
        ssMax = list()
        ssMin = list()
        for i in range(len(l)):
            num = l[i]
            l2 = l[:i] + l[i + 1:]


def sss(l):
    k = 0
    for i in l:
        k += sum(i)
    return k

with open("27-B.txt", "r") as f:
    s = f.read()
s = s.split("\n")
n = int(s[0])
s = s[1:-1]

# pprint.pprint(s)
l = list()
for i in range(n):
    a = s[i].split()
    a1, a2 = int(a[0]), int(a[1])
    l.append([a1, a2])

# pprint.pprint(l)
# exit()
l2 = list()

for i in l:
    if i[0] % 2 != 0:
        l2.append(sorted([i[0], i[1]]))

# pprint.pprint(l2)
# exit()

def chet(l, f):
    k = 0
    for i in l:
        if i[f] % 2 != 0:
            k += 1
    return k

# print(k1n, k1)

l2.sort()
k = 0
# pprint.pprint(l2)
# exit()
l3 = l2[:k] + l2[k + 1:]

while True:
    print(1)
    if k - 1 == len(l2):
        break
    if chet(l3, 0) % 2 != 0:
        l3 = l2[:k] + l2[k + 1:]
        k += 1
    else:
        if chet(l3, 1) % 2 == 0:
            k += 1
        else:
            print(sss(l3))
            exit()
k = 0
l3 = l2[:k] + l2[k + 1:]
while True:
    print(2)
    if k - 1 == len(l2):
        break
    if chet(l3, 1) % 2 == 0:
        l3 = l2[:k] + l2[k + 1:]
        k += 1
    else:
        if chet(l3, 0) % 2 != 0:
            k += 1
        else:
            print(sss(l3))
            exit()



# f = open("27-B.txt")
# n = int(f.readline())
# sum0 = 0
# sum1 = 0
# min1 = 20001
# min2 = 20001
# min3 = 20001
# for i in f:
#     x, y = i.split()
#     x = int(x)
#     y = int(y)
#     if x % 2 == 1:
#         if x > y:
#             sum1 = sum1 + x
#             sum0 = sum0 + y
#             if (x % 2 == 1) and (y % 2 == 1) and ((x + y) < min1):
#                     min1 = x + y
#             if (x % 2 == 0) and (y % 2 == 1) and ((x + y) < min2):
#                     min2 = x + y
#             if (x % 2 == 1) and (y % 2 == 0) and ((x + y) < min3):
#                     min3 = x + y
#         else:
#             sum1 = sum1 + y
#             sum0 = sum0 + x
#             if (x % 2 == 1) and (y % 2 == 1) and ((x + y) < min1):
#                 min1 = x + y
#             if (y % 2 == 0) and (x % 2 == 1) and ((x + y) < min2):
#                     min2 = x + y
#             if (y % 2 == 1) and (x % 2 == 0) and ((x + y) < min3):
#                     min3 = x + y
# if (sum0 % 2 == 0) and (sum1 % 2 == 1):
#     print(sum0 + sum1)
# elif (sum0 % 2 == 1) and (sum1 % 2 == 0):
#     if min1 < min2 + min3:
#         print(sum0 + sum1 - min1)
#     else:
#         print(sum0 + sum1 - min2 - min3)
# elif (sum0 % 2 == 1) and (sum1 % 2 == 1):
#     if min2 < min3 + min1:
#         print(sum0 + sum1 - min2)
#     else:
#         print(sum0 + sum1 - min3 - min1)
# elif (sum0 % 2 == 0) and (sum1 % 2 == 0):
#     if min3 < min2 + min1:
#         print(sum0 + sum1 - min3)
#     else:
#         print(sum0 + sum1 - min2 - min1)

