n = int(input())

s = [sum(list(map(int, input().split()))) for i in range(n)]

# s.sort(key=lambda x: (x[1], x[0]))

print(min(s))
