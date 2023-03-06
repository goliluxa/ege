from itertools import permutations

j = input().split()

n, k = int(j[0]), int(j[1])
# k = 7
numers = list(map(int, input().split()))

if n == k == 1:
    print(numers[0])
elif k == 1 or n == k:
    print(max(numers))
else:
    # m = 0
    # for i in set(permutations(numers, k)):
    #     l = list(i)
    #     l.sort()
    #     # print(l)
    #     if m < l[k // 2]:
    #         m = l[k // 2]
    #
    # print(m)
    numers.sort()
    print(numers[-k:][k // 2])
