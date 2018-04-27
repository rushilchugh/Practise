__author__ = 'Rushil'


def SelectionSort(arr):

    min_index = -1

    for i in range(len(arr)):
        min_elem = 9999999999

        for j in range(i, len(arr)):

            if arr[j] < min_elem:
                min_index = j
                min_elem = arr[j]

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':

    import random

    arr = [random.randint(0,100) for _ in range(10)]
    print(arr)

    SelectionSort(arr)

    print(arr)

