x1, y1, x2, y2, A, B, C = map(int, input().split())

value1 = A * x1 + B * y1 + C

value2 = A * x2 + B * y2 + C

if value1 * value2 > 0:
    print("YES")
else:
    print("NO")
