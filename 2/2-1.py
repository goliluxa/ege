# ((w → ¬x) ≡ (z → y)) /\ (y \/ w)

l = [0, 1]

for x in l:
    for y in l:
        for w in l:
            for z in l:
                f = (((w <= (not x)) == (z <= y)) and (y or w))
                if f and not y:
                    print(x, w, y, z, "-", f, sep="\t")
