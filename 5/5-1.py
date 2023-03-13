print(len({i - int(bin(i)[3:], 2) for i in range(10, 1001)}))
