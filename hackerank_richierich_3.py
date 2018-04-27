__author__ = 'Rushil'

def get_max_palindrome(n,k,str):

    str_list = list(str)

    index = 0

    while k != 0 and index <= n//2:
        num_a = str_list[index]
        num_b = str_list[(n - index) - 1]
        if num_a == '9' and num_b != '9':

            if k >= 1:
                k -=1
            else:
                break

            str_list[(n - index) - 1] = '9'

        elif num_b == '9' and num_a != '9':

            if k >= 1:
                k -=1
            else:
                break

            str_list[index] = '9'

        elif num_b == '9' and num_a == '9':
            pass

        else:
            if k >= 2 and num_a != num_b:
                k -= 2
                str_list[index] = str_list[(n - index) - 1] = '9'
            else:


                if k == 1:
                    if int(num_a) > int(num_b):
                        str_list[(n - index) - 1] = str_list[index]
                        k -= 1

                    elif int(num_a) < int(num_b):
                         str_list[index] = str_list[(n - index) - 1]
                         k -= 1

                    elif num_a == num_b:
                        pass

        index += 1

    if str_list == str_list[::-1]:
        print(''.join(str_list))
    if str_list != str_list[::-1]:
        print(-1)

n,k = tuple(map(int,input().strip().split(' ')))
num = input().strip()
get_max_palindrome(n , k , num)

