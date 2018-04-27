__author__ = 'Rushil'

def pascal(row , col):

    if col == 0:
        return 1

    elif row == col:
        return 1

    else:
        return pascal(row - 1 , col - 1) + pascal(row - 1 , col)

print(pascal(0,0))

