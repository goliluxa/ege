n, m, x, y = map(int, input().split())

print(min(x, y, min(n, m) - x, max(n, m) - y))
