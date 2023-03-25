n = int(input())
a = list(map(int, input().split()))

min_idx = 0
max_idx = 0

for i in range(1, n):
    if a[i] < a[min_idx]:
        min_idx = i
    if a[i] >= a[max_idx]:
        max_idx = i

print(min_idx + 1, max_idx + 1)
