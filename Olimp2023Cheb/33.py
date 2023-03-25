n = int(input())
pasture = []
for i in range(n):
    row = list(map(int, input().split()))
    pasture.append(row)
cow_row = n-1
cow_col = 0
total_calories = pasture[cow_row][cow_col]
while cow_row != 0 or cow_col != n-1:
    if cow_row == 0:
        cow_col += 1
    elif cow_col == n-1:
        cow_row -= 1
    else:
        if pasture[cow_row-1][cow_col] > pasture[cow_row][cow_col+1]:
            cow_row -= 1
        else:
            cow_col += 1
    total_calories += pasture[cow_row][cow_col]
print(total_calories)
