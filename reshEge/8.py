s = "слон"
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    j = i1 + i2 + i3 + i4 + i5
                    if j.count("с") == 1:
                        k += 1

print(k)
