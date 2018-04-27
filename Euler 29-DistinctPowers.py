__author__ = 'Rushil'


def dist_powers():
    a = set()
    for i in range(2,101):
        for j in range(2,101):
            a.add(i**j)
    return a

print(len(dist_powers()))

