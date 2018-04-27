__author__ = 'Rushil'

def dig_sum(n):
    if n%10 == n:
        return n
    else:
        return n%10 + int(dig_sum(n/10))

print(dig_sum(123456))