s = input()
n = len(s)
answer = 0
prev = [s[0], 0]
for i in range(1, n):
    curr = s[i]
    if curr in '1234567890':
        continue
    if prev[0] > curr:
        answer = i + 1
        break
    else:
        prev = [curr, i]

print(answer)
