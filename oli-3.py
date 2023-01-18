m = int(input())
k = int(input())
x = (m // (k + k + 1)) * 2

print(x if x == m else x + 1)

