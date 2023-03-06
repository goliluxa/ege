from itertools import product

#
# c = word.index("c")
# a = word.index("a")
# t = word.index("t")
#
# if c < a < t:
#     word[c] = "C"
#     word[a] = "A"
#     word[t] = "T"
word = input()
c = list()
a = list()
t = list()

for i in range(len(word)):
    w = word[i]
    if w == "c":
        c.append(i)
    elif w == "a":
        a.append(i)
    elif w == "t":
        t.append(i)

# for i in word:

for i1, i2, i3 in product(c, a, t):
    if i1 < i2 < i3:
        word = word[:i1] + word[i1].upper() + word[i1 + 1:i2] + word[i2].upper() + word[i2 + 1:i3] + word[i3].upper() + word[i3 + 1:]
        print(word, sep="")
        break

