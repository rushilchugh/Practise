import math

"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence 
such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for 
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

"""

def LongestIncerase(numList):

    L = [1 for i in range(len(numList))]

    for i in range(len(numList)):
        for j in range(0, i):

            I_Num = numList[i]
            J_Num = numList[j]

            if numList[i] > numList[j] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1

    return L

print(LongestIncerase([10, 22, 9, 33, 21, 50, 41, 60, 80]))

