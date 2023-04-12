# ((x → y) ∨ (y ≡ w)) ∧ ((x ∨ z) ≡ w)


print("Z\tX\tY\tW")

for x in [0, 1]:
    for y in [0, 1]:
        for w in [0, 1]:
            for z in [0, 1]:
                f = (((x <= y) or (y == w))  and ((x or z) == w))
                if f == 1 and sum([x, y, w, z]) != 2 and sum([x, y, w, z]) != 0 and sum([x, y, w, z]) != 4 and sum([w, z]) != 0:
                    print(z, x, y, w, sep="\t")

