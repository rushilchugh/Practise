__author__ = 'Rushil'

num = 0

num_list = []

a = 0
b = 1

while a < 4000000 or b < 4000000:
    num += 10
    #noinspection PyAugmentAssignment
    a = a + b
    b = a + b

    if a%2 == 0:
        num_list.append(a)

    if b%2 == 0:
        num_list.append(b)

print(sum(num_list))

