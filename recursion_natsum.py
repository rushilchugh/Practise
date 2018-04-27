__author__ = 'Rushil'

def nat_sum(n):

    if n != 0:
        return n + nat_sum(n-1)
    else:
        return 0
print(nat_sum(5))