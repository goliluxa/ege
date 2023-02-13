from itertools import product
from numba import njit


@njit
def sta():
    count = 0
    for i1 in "012345678":
        for i2 in "012345678":
            for i3 in "012345678":
                for i4 in "012345678":
                    for i5 in "012345678":
                        for i6 in "012345678":
                            for i7 in "012345678":
                                for i8 in "012345678":
                                    for i9 in "012345678":
                                        g = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9
                                        if g[0] != "2" and g[0] != "4" and g[0] != "6" and g[0] != "0":
                                            if "7777" not in g:
                                                count += 1
    return count


print(sta())
