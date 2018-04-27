__author__ = 'Rushil'

prime_list = [2, 3, 5, 7, 11, 13,]

n = 13

while True:
    flag = 1
    n += 1

    for i in prime_list:
        if n%i == 0:
            flag = 0
            break
    if flag == 1:
        prime_list.append(n)
    if len(prime_list) == 10001:
        print(prime_list[-1])
