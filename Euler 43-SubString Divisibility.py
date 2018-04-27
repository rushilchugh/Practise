__author__ = 'Rushil'

import itertools

div = [2,3,5,7,11,13,17]
n = 0

per_gen = list(itertools.permutations('1234567890'))

#for i in per_gen:
#    print(i)

s = 0

for i in per_gen:
    i = ''.join(i)

    #print(i)

    if i[0] != '0':
        if int(i[1:4]) % 2 == 0:
            if int(i[2:5]) % 3 == 0:
                if int(i[3:6]) % 5 == 0:
                    if int(i[4:7]) % 7 == 0:
                        if int(i[5:8]) % 11 == 0:
                            if int(i[6:9]) % 13 == 0:
                                if int(i[7:10]) % 17 == 0:
                                    s += int(i)
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue

print(s)



