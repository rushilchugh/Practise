__author__ = 'Rushil'

fib_dict = {1:1 , 2:1 , 3:2 , 4:3 , 5:5}

def fib(n):
    if n in fib_dict:
        return fib_dict[n]

    else:
        fib_dict[n] = fib(n-1) + fib(n-2)
        return fib_dict[n]

n = 10
while True:
    if len(str(fib(n))) == 1000:
        break
    n += 1

print(n , fib(n))
