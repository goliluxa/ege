import math

x1, y1, x2, y2 = map(float, input().split())

len1 = (x1 ** 2 + y1 ** 2) ** 0.5
len2 = (x2 ** 2 + y2 ** 2) ** 0.5
dot_product = x1 * x2 + y1 * y2

cos_angle = dot_product / (len1 * len2)
angle = math.acos(cos_angle)

print('{:.5f}'.format(angle))
