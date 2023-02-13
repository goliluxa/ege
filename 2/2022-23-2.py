# ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)

print("Z\tW\tX\tY\tf")
l = [0, 1]

for x in l:
    for y in l:
        for w in l:
            for z in l:
                f = ((x and y) <= ((not z) or w)) and (((not w) <= x) or (not y))
                if f == 0:
                    print(z, w, x, y, f, sep="\t")
