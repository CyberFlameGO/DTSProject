#!/user/bin/env python3.10
"""
Factorial calculation, implemented in 3 functions
"""


def for_factorial(val: int):
    """
    Factorial in for-loop
    :param val:
    :return:
    """
    for i in range(val - 1, 1, -1):
        val *= i
    return val


def while_factorial(val: int):
    """
    Factorial in while-loop
    :param val:
    :return:
    """
    val_mutator = val - 1
    while val != 0:
        val *= val-1
        val -=1
    return val


if __name__ == '__main__':
    print(for_factorial(6))
    print(while_factorial(6))
