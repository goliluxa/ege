n = int(input())

points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

area = 0

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    area += (x1 * y2 - x2 * y1)

area = abs(area) / 2

print("{:.3f}".format(area))
