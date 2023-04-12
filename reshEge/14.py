for x in '0123456789ABCDEFGHI':
    t = int('321' + x + '4', 19) + int('498' + x + '9', 19)
    if t % 23 == 0:
        print(t // 23)
        exit
