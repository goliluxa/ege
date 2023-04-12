l28 = "0123456789ABCDEFJHIJKLMNOPQR"
l13 = "0123456789ABC"

for x in l28:
    for y in l13:
        num1 = "48" + x + "25"
        num2 = "53" + y + "24"

        num1 = int(num1, 28)
        num2 = int(num2, 13)

        num3 = num1 + num2

        if num3 % 113 == 0:
            print(num3 / 113, x, y)
