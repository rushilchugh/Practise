__author__ = 'Rushil'

import itertools
import math

prime_list = []

def check_prime(n):

    if n in prime_list:
        return True

    if n % 2 == 0 and n > 2:
        return False

    j = 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        j = i
        if n % i == 0:
            return False

    if j not in prime_list:
        prime_list.append(j)

    return True



n = 10
perm_list = []

while n < 10000000000:

    num_n  = len(str(n))
    temp_list = []

    for e_dig in range(1,num_n):
        temp_list.append(str(e_dig))

    num = ''.join(temp_list)

    for i in list(itertools.permutations(num)):
        perm_list.append(''.join(i))

    n *= 10

for i in reversed(perm_list):
    let = i[-1]

    if let == '2' or let == '4' or let == '6' or let == '8':
        continue
    else:
        if check_prime(int(i)):
            print(i)
            break
