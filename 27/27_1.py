with open("27-A.txt", "r") as f:
    s = f.read()
s = s.split("\n")
# print(s)
n = int(s[0])

count = 0
# print(n)
a = 0
for i in range(1, n + 1):
    # l = [int(j) for j in s[i - 1] + s[i]]
    a1, a2 = int(s[i - 1]), int(s[i])
    l = a1 + a2
    a3 = a1 * a2
    # l2 = [int(j) for j in str(l)]
    # l2 = [int(j) for j in str(a3)]
    # if l % 3 == 0 and a3 >= 1024 and str(sum(l2))[-1] in "02468":

    if l % 3 == 0 and a3 % 1024 == 0:
        count += 1
        # print(s[i-1])
    a += 1
print(count, a)

# 145
# 239352
