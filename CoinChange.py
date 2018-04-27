import math
import sys

def minCoins(cList, S):
    Min = [math.inf for _ in range(S)]

    Min[0] = 0

    for i in range(1, S):
        currentState = i

        for j in range(0, len(cList)):
            currentCoin = j

            if cList[j] <= i and Min[i - cList[j]] + 1 < Min[i]:
                Min[i] = 1 + Min[i - cList[j]]

    return Min

minCoins([1, 7, 10], 15)

def minCoinsRECUR(cList, S):

    finalAns = math.inf

    if S == 0:
        return 0
    
    for i in range(0, len(cList)):
        if cList[i] <= S: 
            coinsNeeded = 1 + minCoinsRECUR(cList, S - cList[i])

            finalAns = min(finalAns, coinsNeeded)

    return finalAns
