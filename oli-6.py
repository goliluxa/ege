l = "A, Б, В, Г, Д".split(", ")
d = set()
for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                for i5 in l:
                    for i6 in l:
                        for i7 in l:
                            s = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            if s.count("A") == 1 and s.count("В") == 1:
                                if s.count("Д") <= 1:
                                    d.add(s)

print(len(d))
