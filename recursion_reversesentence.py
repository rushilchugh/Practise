__author__ = 'Rushil'

def rev(str):
    str_list = str.split(' ')
    if len(str_list) != 1:
        return str_list[-1] + ' ' + rev(' '.join(str_list[:-1]))
    else:
        return str_list[0]

print(rev('Here are a few practice questions for recursion'))
