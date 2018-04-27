def CoinChange(cList, S):

    minCoins = [999999 for _ in range(S + 1)]

    minCoins[0] = 0

    for i in range(1, S + 1):
        currentState = i
        
        for j in range(0, len(cList)):
            currentCoinIndex = j

            if cList[j] <= i and 1 + minCoins[i - cList[j]] < minCoins[i]:
                 minCoins[i] = 1 + minCoins[i - cList[j]]

    return minCoins

nCoins, S = map(int, input().split())
coinList = list(map(int, input().split()))

mCoins = CoinChange(coinList, S)

print(mCoins[S])

