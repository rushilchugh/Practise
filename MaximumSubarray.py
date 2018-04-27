import math

def MaximumSubarray(A):

    MaxSum = [-math.inf for _ in range(len(A))]
    MaxSum[0] = A[0]

    for i in range(1, len(A)):
        for j in range(0, i):
            if MaxSum[j] + A[i] > MaxSum[i]:
                MaxSum[i] = MaxSum[j] + A[i]

    return MaxSum






A = [-2, -3, 4, -1, -2, 1, 5, -3]
print(MaximumSubarray(A))

