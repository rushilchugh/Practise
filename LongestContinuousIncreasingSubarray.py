def longestContSubseq(seqList):

    S = [1 for _ in range(len(seqList))]

    for i in range(1, len(seqList)):
        if seqList[i] > seqList[i - 1]:
            S[i] = S[i - 1] + 1

        else:
            S[i] = 1

    return S

print(longestContSubseq([10, 22, 9, 33, 21, 50, 41, 60, 80]))
