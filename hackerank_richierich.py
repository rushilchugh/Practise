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

def get_max_palindrome(k , sub_1 , sub_2 , mid_em = ''):

    n_sub_1 = list(sub_1)
    n_sub_2 = list(sub_2)

    sub_length = len(sub_1) - 1
    index_count = 0

    while k > 0 and sub_length >= 0:
        num_a = int(sub_1[sub_length])
        num_b = int(sub_2[index_count])

        if num_a > num_b:
            n_sub_2[index_count] = n_sub_1[sub_length]
            k -= 1

        elif num_a < num_b:
            n_sub_1[sub_length] = n_sub_2[index_count]
            k -=1

        elif num_a == num_b:
            n_sub_1[sub_length] = n_sub_2[index_count] = '9'
            k -= 2

        index_count += 1
        sub_length -= 1



        #print(num_a,num_b)

    if n_sub_1 == n_sub_2[::-1]:
        if mid_em == '':
            return ''.join(n_sub_1) + ''.join(n_sub_2)
        if mid_em != '':
            return ''.join(n_sub_1) + mid_em + ''.join(n_sub_2)
    else:
        return -1

def get_max_palindrome_2(k , sub_1 , sub_2 , mid_em = ''):

    f = 0
    r = -1

    n_sub_1 = list(sub_1)
    n_sub_2 = list(sub_2)

    while k > 0:
        num_a = int(sub_1[f])
        num_b = int(sub_2[r])

        if num_a > num_b:
            if k > 1:
                n_sub_2[r] = n_sub_1[f] = '9'
                k -= 2

        elif num_a < num_b:
            n_sub_1[f] = n_sub_2[r]

        elif num_a == num_b:
            n_sub_1[sub_length] = n_sub_2[index_count] = '9'

        f += 1
        r -= 1

        k -= 1

        #print(num_a,num_b)

    if n_sub_1 == n_sub_2[::-1]:
        if mid_em == '':
            return ''.join(n_sub_1) + ''.join(n_sub_2)
        if mid_em != '':
            return ''.join(n_sub_1) + mid_em + ''.join(n_sub_2)
    else:
        return -1





k = int(input().strip().split(' ')[-1])
n = input()
print(get_max_palindrome(k , *get_substrings(n)))

#print(get_max_palindrome(10 , *get_substrings('0111')))
#
#print('--'*60)
#
#print(get_substrings('98765432'))
#get_max_palindrome(*get_substrings('98765432'),5)
