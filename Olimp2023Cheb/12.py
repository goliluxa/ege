n = int(input())
votes = input().split()

candidates = {}

for vote in votes:
    if vote in candidates:
        candidates[vote] += 1
    else:
        candidates[vote] = 1

winner = max(candidates, key=candidates.get)

print(winner)
