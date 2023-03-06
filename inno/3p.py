from itertools import combinations, product, permutations
import re

def go(s, t):
    pattern = re.compile('(?=(' + re.escape(s) + '))')

    result = pattern.findall(t)
    return len(result)

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

#
# l = "abacaba"
# l2 = "abc"

l = input()
l2 = input()
# a =
k = 0
# print(len(l2))
s = list()
s2 = set()

for j in range(1, len(l2) + 1):
    for i in set(permutations(l2, j)):
        p = "".join(i)
        if len(p) > 1 and len(set(p)) != len(p) and l.find(p) != l.rfind(p):
            a = go(p, l)
        else:
            a = l.count(p)
        if a > 0 and all(l2.count(b) >= p.count(b) for b in p):
            # print(p)
            # print(p, a)
            k += a

print(k)

# c
# a
# b
# ca
# ba
# ac
# ab
# cab
# bac
# 15
