__author__ = 'Rushil'

def count8(n):
    if n == 0:
        return 0
    if n%10 == 8 and n%100 != 88:
        return 1 + count8(n//10)
    elif n%100 == 88:
        return 3 + count8(n//100)
    else:
        return count8(n//10)


print(count8(88188))