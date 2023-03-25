
n, *t = map(int, input().split())

def total_time(order):
    time = 0
    for i in range(n):
        time += t[order[i]] * (i+1)
    return time

orders = [[i] for i in range(n)]
for i in range(1, n):
    new_orders = []
    for order in orders:
        for j in range(n):
            if j not in order:
                new_orders.append(order + [j])
    orders = new_orders

min_time = float('inf')
min_order = []
for order in orders:
    time = total_time(order)
    if time < min_time:
        min_time = time
        min_order = order

print(min_time)
print(' '.join(str(i+1) for i in min_order))
