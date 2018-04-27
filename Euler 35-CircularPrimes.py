__author__ = 'Rushil'

from collections  import deque
import math
import time

t_1 = time.time()

def get_rot_elems(n):

    m_list = []
    n_list = deque(list(map(int , list(str(n)))))

    for i in range(len(n_list)):

        n_list.rotate()
        m_list.append(list(n_list))

    return m_list

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

def get_num_list(n):
    return list(map(int , [''.join(list(map(str , j))) for j in get_rot_elems(n)]))

def check_prime_list(num_list):
    while len(num_list):
        min_num = num_list[0]
        if check_prime(min_num):
            num_list.remove(min_num)
        else:
            break

s = 0

all_nums = [[2]]


for i in range(3,1000000):

    if i % 2 == 0:
        continue


    a = sorted(get_num_list(i))

    if a not in all_nums:
        check_prime_list(a)

        if len(a) == 0:
            all_nums.append(sorted(get_num_list(i)))

m_set = set()

for i in all_nums:
    for j in i:
        m_set.add(j)

print(len(m_set))

t_2 = time.time()

print("Done in Time: " , t_2 - t_1)

#for i in range(1000000):
#    print(i,check_prime(i),prime_list)