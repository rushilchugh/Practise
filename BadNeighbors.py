import math

def BadNeighbors(nDons):

    # RecursiveRelation
    # maxDonations[n] = max(nDons[n] + maxDonations[n - 2] | maxDonations[n - 1])

    maxDonations = [nDons[i] for i in range(len(nDons))]

    for i in range(2, len(nDons)):
        for j in range(0, i-1):                 #It only iterates until i-2
            if maxDonations[j] + nDons[i] > maxDonations[i]:
                maxDonations[i] = maxDonations[j] + nDons[i]

            else:
                maxDonations[i] = maxDonations[i-1]


        """"
        Try 2
        if maxDonations[i - 2] + nDons[i] > maxDonations[i - 1]:
            maxDonations[i] = maxDonations[i - 2] + nDons[i]
        else:
            maxDonations[i] = maxDonations[i - 1]
        """

        """"
        Try 1
        if i % 2 == 0:
            for j in range(0, i):
                if maxDonations[j] + nDons[i] > maxDonations[i]:
                    maxDonations[i] = maxDonations[j] + nDons[i]

        elif i % 2 == 1:
            for j in range(1, i, 2):
                if maxDonations[j] + nDons[i] > maxDonations[i]:
                    maxDonations[i] = maxDonations[j] + nDons[j]
        """

    return maxDonations

qList = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
a = BadNeighbors(qList)
print(a)
print(list(zip(qList, a)))