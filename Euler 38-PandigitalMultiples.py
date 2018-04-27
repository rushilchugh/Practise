__author__ = 'Rushil'

product_list = sorted(list('123456789'))
print(product_list)

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576

#9 x 1 = 9
#9 x 2 = 18
#9 x 3 = 27
#9 x 4 = 36
#9 x 5 = 45

#19 x 1 = 19
#19 x 2 = 38
#19 x 3 = 57
#19 x 4 = 76

for i in range(1,10000):
    num_list = []
    for j in range(1,11):
        prod = str(i*j)

        if '0' in prod:
            break

        num_list += list(prod)

        if  sorted(num_list) == product_list:
            break

    if len(num_list) == 9 and sorted(num_list) == product_list:
        print(i,''.join(num_list) , j)
