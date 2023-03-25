n, m = map(int, input().split())
defective = list(map(int, input().split()))

intervals = []
start = defective[0]
for i in range(1, m):
    if defective[i] - defective[i - 1] > 1:
        intervals.append((start, defective[i - 1]))
        start = defective[i]
intervals.append((start, defective[-1]))

output = ""
for interval in intervals:
    if interval[0] == interval[1]:
        output += str(interval[0])
    else:
        output += str(interval[0]) + "-" + str(interval[1])
    output += ","
output = output[:-1]
print(output)
