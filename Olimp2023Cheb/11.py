n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_main = 0
sum_secondary = 0

for i in range(n):
    sum_main += matrix[i][i]
    sum_secondary += matrix[i][n - 1 - i]

print(sum_main)
print(sum_secondary)
