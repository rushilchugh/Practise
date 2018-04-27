import math

def CoinChange(cList, S):
    LC = [math.inf for _ in range(S)]
    LC[0] = 0

    for i in range(1, S):
        for j in range(len(cList)):
            if i >= cList[j] and LC[i - cList[j]] + 1 < LC[i]:
                LC[i] = LC[i - cList[j]] + 1

    return LC
