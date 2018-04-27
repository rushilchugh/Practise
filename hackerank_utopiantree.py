__author__ = 'Rushil'

n = int(input().strip())

n_cycles = [input() for i in range(n)]

n_cycles = list(map(int , n_cycles))

for cycle in n_cycles:
    s = 1
    if cycle == 0:
        print(s)
    else:
        for i in range(1,cycle+1):
            if i % 2 != 0:
                s *= 2
            if i % 2 == 0:
                s += 1
        print(s)
