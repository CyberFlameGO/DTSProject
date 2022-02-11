#!/user/bin/env python3.10
"""
Bubble sorting
"""


def bubble_sort(arr: list):
    """
    Sorts an array (list) using bubble sorting
    :param arr:
    """
    n = len(arr)

    for i in range(0, n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array_test = [1, 2, 6, 3, 2, 5, 6, 77, 3, 21, 4]
bubble_sort(array_test)

print(array_test)
