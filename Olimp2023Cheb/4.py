x1, y1, x2, y2, x3, y3 = map(int, input().split())

x4 = x3 + x1 - x2
y4 = y3 + y1 - y2

x5 = x1 + x2 - x3
y5 = y1 + y2 - y3

x6 = x2 + x3 - x1
y6 = y2 + y3 - y1

print(x5, y5, x6, y6, x4, y4)
