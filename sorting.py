#!/user/bin/env python3.10
"""
Bubble sorting
"""


# swap_count: int = 0

def bubble_sort(array: list) -> object:
    """
    Sorts an array (list) using bubble sorting
    :param array:
    :rtype: object
    :return: tuple
    """
    n = len(array)
    sorted_array = array.copy()

    swap_count = 0
    for i in range(0, n - 1):
        for j in range(n - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                swap_count += 1
    return sorted_array, swap_count


array_test = [1, 2, 6, 3, 2, 5, 6, 77, 3, 21, 4, 8]

sorted_arr, num_swaps = bubble_sort(array_test)
print("Unsorted list: ", array_test, "\nSorted list: ", sorted_arr, f"\nSwap count: {num_swaps}", sep = "")
