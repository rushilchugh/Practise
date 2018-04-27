__author__ = 'Rushil'


fact_dict = {}
def fact(n):
    if n == 1:
        return 1
    else:
        fact_dict[n] = n * fact(n-1)
        return fact_dict[n]

