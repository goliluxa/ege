import time

t = time.time()

# from fnmatch import fnmatch
# from functools import reduce
#
# data = open("17-346.txt").read().split("\n")
#
# count, pows = 0, []
#
# for i in range(len(data) - 2):
#     a, b, c = data[i], data[i + 1], data[i + 2]
#     mas = [int(i) for i in (a + b + c) if int(i) % 2 == 0]
#     pow = reduce(lambda x, y: x * y, mas, 1)
#
#     if pow <= 2 * 10 ** 9 and fnmatch(str(pow), "11*6*"):
#         count += 1
#         pows.append(pow)
#
# print(count, max(pows))

# data = open("17-346.txt").read().split("\n")
#
#
# def check_mask(num):
#     if str(num)[:2] == "11" and "6" in str(num)[2:]:
#         return True
#     else:
#         return False
#
#
# def Pow(a, b, c):
#     s = str(a) + str(b) + str(c)
#     pow = 1
#     for i in s:
#         if int(i) % 2 == 0:
#             pow *= int(i)
#     return pow
#
#
# count = 0
# mas = []
#
# for i in range(len(data) - 2):
#     pow = Pow(data[i], data[i + 1], data[i + 2])
#     result = pow <= 2 * 10 ** 9 and check_mask(pow)
#
#     if result:
#         count += 1
#         mas.append(pow)
#
# print(count, max(mas))

# from fnmatch import fnmatch
# from functools import reduce
#
# data = [int(x) for x in open("17-346.txt")]
#
# count, pows = 0, []
#
# for i in range(len(data) - 2):
#     a, b, c = str(data[i]), str(data[i + 1]), str(data[i + 2])
#     mas = [int(i) for i in (a + b + c) if int(i) % 2 == 0]
#     pow = reduce(lambda x, y: x * y, mas, 1)
#
#     if pow <= 2 * 10 ** 9 and fnmatch(str(pow), "11*6*"):
#         count += 1
#         pows.append(pow)
#
# print(count, max(pows))
print(time.time() - t)
