for i in range(1000):
    bi = bin(i)[2:]
    oc = oct(i)[2:]
    he = hex(i)[2:]
    try:
        if bi[:2] == "10" and oc[1] == "4" and he[1] == "2" and \
                len(bi) == 8 and len(oc) == 3 and len(he) == 2:
            print(i)
    except:
        pass
