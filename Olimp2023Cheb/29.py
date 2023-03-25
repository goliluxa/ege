n = int(input())
a = list(map(int, input().split()))

k = 0
flag1 = True
flag2 = True
for i in range(1, n):
    if a[i - 1] < a[i]:
        if flag1 or flag2:
            k += 1
            flag1 = False
            if not flag1:
                flag2 = False
    else:
        flag1 = True
        flag2 = True
print(k)
