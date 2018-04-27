__author__ = 'Rushil'

def sieve(n):
    num_list = [True] * n

    num_list[0] = num_list[1] = False

    for i,j in enumerate(num_list):
        if j:
            yield i
            for num in range(i*i,n,i):
                num_list[num] = False

print(sum(list(sieve(2000000))))
