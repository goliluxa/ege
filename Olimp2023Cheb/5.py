num = int(input())

digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10

sum_digits = digit1 + digit2 + digit3 + digit4
prod_digits = digit1 * digit2 * digit3 * digit4

print(sum_digits)
print(prod_digits)
