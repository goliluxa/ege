# (𝑥+𝐴≥85)∨(ДЕЛ(𝑥,7)→ДЕЛ(𝑥,9))

for A in range(1000):
    if all(((x + A >= 85) or (x % 7 == 0) <= (x % 9 == 0)) for x in range(1, 1000)):
        print(A)
