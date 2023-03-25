x1, y1, x2, y2, a, b, c = map(int, input().split())

value1 = a * x1 + b * y1 + c

value2 = a * x2 + b * y2 + c

if value1 * value2 > 0:
    print("YES")
else:
    print("NO")
