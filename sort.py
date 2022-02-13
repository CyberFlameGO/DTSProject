#!/user/bin/env python3.10
"""
Sorting
"""


class Sort:
    """
    Sorting
    """

    # swap_count: int = 0

    def bubble_sort(self: list) -> object:
        """
        Sorts an array (list) using bubble sorting
        :param self:
        :rtype: object
        :return: tuple
        """
        n = len(self)
        sorted_array = self.copy()

        swaps: int = 0
        comparisons: int = 0
        for i in range(0, n - 1):
            for j in range(n - i - 1):
                comparisons += 1
                if sorted_array[j] > sorted_array[j + 1]:
                    sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                    swaps += 1
        return sorted_array, swaps, comparisons

    def min_selection_sort(self: list) -> object:
        """
        Sorts an array (list) using minimum selection sorting
        :param self:
        :rtype: object
        :return: list
        """
        sorted_array: list = self.copy()
        for i in range(len(sorted_array)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(sorted_array)):
                if sorted_array[min_idx] > sorted_array[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            sorted_array[i], sorted_array[min_idx] = sorted_array[min_idx], sorted_array[i]
        return sorted_array


array_test = [1, 2, 6, 3, 2, 5, 6, 77, 3, 21, 4, 8, 0.5, 0, 1, 1, 1, 132455454, 565656]

sorted_arr, num_swaps, comparison_count = Sort.bubble_sort(array_test)
print("Unsorted list: ", array_test, "\nSorted list: ", sorted_arr, f"\nSwap count: {num_swaps}\nComparison count: "
                                                                    f"{comparison_count} ", sep = "")
print()
print("Unsorted list:", array_test, "\nSorted list:", Sort.min_selection_sort(array_test))
