__author__ = 'Rushil'

import operator
import sys

sys.setrecursionlimit(15000)


(n,k) = tuple(map(int ,  input().strip().split()))
p_list = list(map(int , input().strip().split()))

#This works, although reaches recursion depth and runtime error, so.....Nevermind, cool solution though !!
def do_stuff_2(elem_list, offset , k):

    if k == 0:
        return None

    if offset + 1 >= len(elem_list):
        return None

    max_index , max_element = max(enumerate(elem_list[offset:]) , key = operator.itemgetter(1))
    max_index += offset
    elem_list[max_index],elem_list[offset] = elem_list[offset],elem_list[max_index]
    k -= 1

    return do_stuff_2(elem_list , offset+1,k)

do_stuff_2(p_list,0,k)

for i in p_list:
    print(i , end = ' ')
