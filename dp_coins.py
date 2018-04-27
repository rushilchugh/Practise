__author__ = 'Rushil'

#Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S
#(we can use as many coins of one type as we want), or report that it’s not possible to select coins in such a way that they sum up to S.

from collections import defaultdict


def min_coins(s,v):
    min_dict = defaultdict(int)

    min_dict[0] = 0

    for i in range(1,s+1):
        min_dict[i] = 999
        for j in range(len(v)):
            if (v[j] <= i) and ((min_dict[i - v[j]] + 1) < min_dict[i]):
                min_dict[i] = min_dict[i - v[j]] + 1

    return min_dict

for i,j in min_coins(5,[1,3,5]).items():
    print(i,j)

print('--'*60)

def min_coins_2(s,n):

    if s == 0:
        return 0

    return

