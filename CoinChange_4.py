
import math

"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} 
valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
So the output should be 5.
"""

def CoinChange(cList, S):

    mCoins = [math.inf for _ in range(S + 1)]
    mCoins[0] = 0

    for i in range(1, S + 1):
        for j in range(len(cList)):
            if mCoins[i - cList[j]] + 1 < mCoins[i] and cList[j] <= i:
                mCoins[i] = mCoins[i - cList[j]] + 1

    return mCoins

print(CoinChange([1, 2, 3], 4))
