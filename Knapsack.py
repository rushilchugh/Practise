def Knapsack(Weights, Prices, N, W):

    if N == 0 or W == 0:
        return 0

    else:
        if Weights[N - 1] < W:
            prIncluded = Prices[N - 1] + Knapsack(Weights, Prices, N - 1, W - Weights[N - 1])

        else:
            prIncluded = 0

        prNotIncluded = 0 + Knapsack(Weights, Prices, N - 1, W)

        return max(prIncluded, prNotIncluded)


print(Knapsack([2, 7, 3, 4], [5, 20, 20, 10], 4, 11))