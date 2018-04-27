__author__ = 'Rushil'

w_list = open('wordlist.txt' , 'r')

for i in w_list.readlines():
    if 'cal' in i:
        print(i)

w_list.close()