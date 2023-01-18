f = open("files/k7-m4.txt", "r")

a = f.read() + "*"
s1 = 0
k = 1
g = ""
for i in a:
    if i == "C":
        s1 += 1
    else:
        if 0 < s1 <= 4:
            g += f'{s1}{"c" * s1}'
            k += 1
        s1 = 0
        g += i
