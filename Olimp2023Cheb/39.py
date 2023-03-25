x1, y1, x2, y2, x3, y3 = map(int, input().split())

a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
    print(2)
else:

    cos_a = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    cos_b = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    cos_c = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    if cos_a > 0 and cos_b > 0 and cos_c > 0:
        print(3)

    elif cos_a < 0 or cos_b < 0 or cos_c < 0:
        print(1)

    else:
        print(0)
