__author__ = 'Rushil'

def stairs(n):
    for i in range(1,n+1):
        print(' '*(n-i) + '#'*i)

stairs(5)