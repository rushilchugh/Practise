__author__ = 'Rushil'

"""
Given an M x N grid, find the total number of ways to move from the bottom-left corner to the rop-right corner
"""


#1 - Total Paths, Basic Recursion
def TotalPaths(m, n):
    if m == 0 or n == 0:
        return 1

    else:
        return TotalPaths(m - 1, n) + TotalPaths(m, n - 1)

#print(TotalPaths(2, 2))


#2 Total Paths, Memoization
subprobs = {(0, 0): 0}


def TotalPaths_Memoized(m, n):

    global subprobs

    if (m, n) in subprobs:
        return subprobs[(m, n)]

    if 0 in (m, n) and (m, n) not in subprobs:
        subprobs[(m, n)] = 1
        return subprobs[(m, n)]

    else:
        subprobs[(m, n)] = TotalPaths_Memoized(m - 1, n) + TotalPaths_Memoized(m, n - 1)

TotalPaths_Memoized(2, 2)
print(subprobs)