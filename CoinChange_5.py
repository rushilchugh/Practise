import math

def coinChange(cList, S):

    minVals = [math.inf for _ in range(S + 1)]
    minVals[0] = 0

    for i in range(1, S + 1):
        for j in range(len(cList)):
            currCoin = cList[j]
            if cList[j] <= i and minVals[i - cList[j]] + 1 < minVals[i]:
                minVals[i] = minVals[i - cList[j]] + 1

    return minVals

print(coinChange([1, 5, 7], 8))