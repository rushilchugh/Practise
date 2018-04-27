__author__ = 'Rushil'

def sieve(n):
    num_list = [True] * n

    num_list[0] = num_list[1] = False

    for i,j in enumerate(num_list):
        if j:
            yield i
            for num in range(i*i , n , i):
                num_list[num] = False

def get_num_list(n):

    n1 = str(n)

    while n:
        yield n
        n //= 10

    while len(n1) != 1:
        yield int(n1[1:])
        n1 = n1[1:]



p_list = list(sieve(100000))

print('Sieve Made')

t_prime_list = list(zip(p_list , [True]*100000))
print('Prime List Made')

t_prime_list = [list(i) for i in t_prime_list]

for index,i in enumerate(t_prime_list):

    for num in get_num_list(i[0]):
        if num not in p_list:
            t_prime_list[index][1] = False

            break
        else:
            pass
print('--'*60)


s = 0

for i in t_prime_list[4:]:
    if i[1]:
        s += i[0]
        print(i[0])

print(t_prime_list)