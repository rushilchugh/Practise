__author__ = 'Rushil'

#num_list = list(map(int , input().strip().split(' ')))


#Recursion = func(n) = func(n-1)^2 + func(n-2)
main_dict = {1: 1, 2: 1}

def func(a,b,n):

    if n == 2 :
        print(main_dict)
        return main_dict[2]

    else:
        if n in main_dict.keys():
            print(main_dict)
            return main_dict[n]

        else:
            main_dict[n] = func(a,b,n-1)**2 + func(a,b,n-2)
            print(main_dict)
            return main_dict[n]


print(func(1,1,35))

