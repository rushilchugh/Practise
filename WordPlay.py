__author__ = 'Rushil'

f_list = open('wordlist.txt' , 'r')

f_list.seek(0)
for i in f_list.readlines():
    if i.endswith('ies\n'):
        print(i)

f_list.close()