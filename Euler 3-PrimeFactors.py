__author__ = 'Rushil'

prime_factors = [2,3]

num = 600851475143
range_var = int(num/2)

def check_prime(n):
    flag = 1

    range_arg = int(n/2)

    for i in range(2,range_arg):
        if n%i == 0:
            flag = 0
            break

    if flag == 1:
        prime_factors.append(n)

for i in range(5,range_var):
    if num%i == 0:
        check_prime(i)
        print(prime_factors[-1])


