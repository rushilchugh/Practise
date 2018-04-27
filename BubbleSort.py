__author__ = 'Rushil'


def BubbleSort(arr):

    n = len(arr)
    for i in range(n - 1):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


if __name__ == '__main__':

    import random

    arr = [random.randint(0,100000) for _ in range(100)]
    print(arr)

    BubbleSort(arr)

    print(arr)

