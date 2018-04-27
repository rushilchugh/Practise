__author__ = 'Rushil'

import operator

(n,k) = tuple(map(int , input().strip().split()))
p_list = list(map(int , input().strip().split()))

#def do_stuff(elem_list):
#
#    if not elem_list:
#        return None
#
#    max_index , max_element = max(enumerate(elem_list) , key = operator.itemgetter(1))
#    elem_list[max_index],elem_list[0] = elem_list[0],elem_list[max_index]
#
#    return do_stuff(elem_list[1:])



#This works !!
def do_stuff_2(elem_list, offset , k):

    if k == 0:
        return None

    if offset + 1 >= len(elem_list):
        return None

    max_index , max_element = max(enumerate(elem_list[offset:]) , key = operator.itemgetter(1))
    max_index += offset             #max_index with respect to the original list, rather than the sub-list, for instance if the theoretical list slice
                                    #being worked upon is 2 3 4 1, when 4 and 2 are swapped, max_index is the position of 4 with respect to the
                                    #original list, and that solves the problem

                                    #also note that list slices do not extract items from the list, instead the return a copy of the list
                                    #that is an entirely different entity

    elem_list[max_index],elem_list[offset] = elem_list[offset],elem_list[max_index]
    k -= 1
    return do_stuff_2(elem_list , offset+1,k)

def sortl(l, last):
    # base case
    if last + 1 >= len(l):
         return l
    # find the max_index and max value in the list
    mi, _ = max(enumerate(l[last:]), key = operator.itemgetter(1))
    mi += last # caculate the offset in the sublist
    l[mi], l[last] = l[last], l[mi] # swap the values

    # recursive call
    return sortl(l, last + 1)


do_stuff_2(p_list,0,k)

for i in p_list:
    print(i , end = ' ')