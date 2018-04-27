__author__ = 'Rushil'

from collections import Counter

inp_str = input().strip()

def check_pairing(tst_str):
    n_0 = 0
    a = Counter(tst_str)

    for i,j in a.items():
        if j % 2 != 0:
            n_0 += 1

    if n_0 > 1:
        return 'NO'

    return 'YES'


print(check_pairing(inp_str))

