for A in range(100000):
    if all(((((x <= 9) >= (x * x <= A)) and ((y * y <= A) >= (y <= 9))) for x in range(10000)) for y in range(10000)):
        print(A)
        break
