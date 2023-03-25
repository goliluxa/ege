field = []
for i in range(10):
    row = list(map(int, input().split()))
    field.append(row)
max_length = 0
for i in range(10):
    for j in range(10):
        if field[i][j] == 0:
            length = 0
            while j + length < 10 and field[i][j + length] == 0:
                length += 1
            max_length = max(max_length, length)
            # check vertical length
            length = 0
            while i + length < 10 and field[i + length][j] == 0:
                length += 1
            max_length = max(max_length, length)
print(max_length)
