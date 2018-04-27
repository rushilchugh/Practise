__author__ = 'Rushil'

def fun_eh(str1):

    str2 = str1[::-1]

    for i in range(1,len(str1)):
        if abs(ord(str1[i]) - ord(str1[i-1])) != abs(ord(str2[i]) - ord(str2[i-1])):
            return 'Not Funny'

    return 'Funny'

n = int(input().strip())
str_list = [input().strip() for i in range(n)]

for i in str_list:
    print(fun_eh(i))