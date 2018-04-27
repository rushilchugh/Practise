__author__ = 'Rushil'

num_list = []

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        num_list.append(i)
    else:
        pass

print(sum(num_list))
