def funk(n):
    n1 = list(map(int, list(bin(n)[2:])))
    if n % 2 != 0:
        n1 = [1] + n1 + [1, 1]
    else:
        n1 = [1, 1] + n1 + [0, 0]
    s = ""
    for i in n1:
       s += str(i)
    return int(s, 2)
s = []
for i in range(100):
    n = funk(i)
    if n < 127:
        s.append(n)
        
print(max(s))

