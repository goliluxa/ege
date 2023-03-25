n = int(input())
a = list(map(int, input().split()))

even = []
odd = []

for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

for num in even:
    print(num, end=" ")

for num in reversed(odd):
    print(num, end=" ")
