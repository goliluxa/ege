f = open("files/k7-m3.txt", "r")

a = f.read() + "*"
s1 = 0
k = 1

for i in a:
    if i == "C":
        s1 += 1
    else:
        if 0 < s1 <= 4:
            print(k, s1, "C" + "c" * (s1 - 1))
            k += 1
        s1 = 0
