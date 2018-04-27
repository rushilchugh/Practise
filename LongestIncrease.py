def LongestIncrease(cList):

    L = [1 for _ in range(len(cList))]

    for i in range(1, len(cList)):
        for j in range(0, i):
            e1 = cList[i]
            e2 = cList[j]
            if cList[i] > cList[j] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1

    return L
print(LongestIncrease([50, 3, 10, 7, 40, 80]))