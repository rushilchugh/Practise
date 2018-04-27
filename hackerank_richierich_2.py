__author__ = 'Rushil'

def get_substrings(n):
    len_n = len(n)

    if len_n % 2 == 0:
        sub_1 = n[0:len_n//2]
        sub_2 = n[len_n//2:]
        return sub_1,sub_2

    elif len_n % 2 != 0:
        sub_1 = n[0:len_n//2]
        sub_2 = n[len_n//2 + 1:]
        return sub_1,sub_2,n[len_n//2]

#print(get_substrings('123456789'))
#print(get_substrings('987654321'))


def get_max_palindrome(sub_len , k , sub_1 , sub_2 , mid_em = ''):
    print(sub_len)

    sub_list_1 = list(sub_1)
    sub_list_2 = list(sub_2)

    for index,num in enumerate(sub_1):
        num_a = sub_1[index]
        num_b = sub_2[(sub_len//2 - index) - 1]

        print(num_a,num_b)

        if num_a == '9' and num_b != '9':

            if k >= 1:
                k -=1
            else:
                break

            sub_list_2[(sub_len//2 - index) - 1] = '9'

        elif num_b == '9' and num_a != '9':

            if k >= 1:
                k -=1
            else:
                break

            sub_list_1[index] = '9'


        elif num_b == '9' and num_a == '9':
            pass

        else:
            pass

def get_max_palindrome_2(s_len , k , s):
    pass



len_n,k = tuple(map(int,input().strip().split(' ')))
n = input()
print(get_max_palindrome(len_n , k , *get_substrings(n)))

