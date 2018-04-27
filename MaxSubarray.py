__author__ = 'Rushil'


def Kadanes_MaxSubarray(arr):

    max_until_here = max_so_far = arr[0]

    arr_n = arr[1:]

    for i in arr_n:

        max_until_here = max(i, max_until_here + i)
        max_so_far = max(max_until_here, max_so_far)

    return max_so_far

print(Kadanes_MaxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))