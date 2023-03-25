n = int(input())
fib1 = 1
fib2 = 1
if n == 1 or n == 2:
    print("True")
else:
    while fib2 < n:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
    if fib2 == n:
        print("True")
    else:
        print("False")
