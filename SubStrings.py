def FindOccurence(str1, str2):
    len_1 = len(str1)
    len_2 = len(str2)

    commonTable = [[0 for i in range(len_2 + 1)] for j in range(len_1 + 1)]

    for i in range(len_2 + 1):
        commonTable[0][i] = 0

    for i in range(len_1 + 1):
        commonTable[i][0] = 1

    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if str1[i - 1] == str2[j - 1]:
                commonTable[i][j] = commonTable[i - 1][j - 1] + commonTable[i - 1][j]

            else:
                commonTable[i][j] = commonTable[i - 1][j]

    return commonTable[len_1][len_2]

mainStr = input()

T = int(input())

for i in range(T):
    print(FindOccurence(mainStr, input()))




