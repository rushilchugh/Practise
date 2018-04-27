__author__ = 'Rushil'

import time

def p_sieve(n):
    num_list = [True] * n

    num_list[0] = num_list[1] = False

    for i,j in enumerate(num_list):
        if j:
            yield i

            for num in range(i*i , n , i):
                num_list[num] = False


n = 1000000
sieve_list = list(p_sieve(n))


def gen_trunc_primes():
    p_list = sieve_list

    p_dict = dict(zip(p_list ,[True]*n ))
    #print(p_dict)

    for num in p_list:
        str_num = str(num)
        if '2' in str_num or '4' in str_num or '6' in str_num or '8' in str_num or '0' in str_num :
            p_dict[num] = False

    p_dict[2] = p_dict[3] = p_dict[5] = p_dict[7] = True
    p_dict[23] = True

    for i,j in p_dict.items():
        if j:
            yield i

def make_num_list(num):
    str_num_1 = str_num_2 = str(num)

    yield num

    while len(str_num_1) != 1:
        yield int(str_num_1[1:])
        str_num_1 = str_num_1[1:]

    while len(str_num_2) != 1:
        yield int(str_num_2[:-1])
        str_num_2 = str_num_2[:-1]

trunc_prime_set = set(gen_trunc_primes())

def main():
    for i in gen_trunc_primes():
        num_set = set(make_num_list(i))
        if num_set.intersection(trunc_prime_set) == num_set and i != 2 and i != 3 and i != 5 and i != 7 :
            yield i

t_1 = time.time()
print(sum(list(main())))
t_2 = time.time()
print('Time Taken = ' , t_2 - t_1)