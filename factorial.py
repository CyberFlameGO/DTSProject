#!/user/bin/env python3.10
"""
Factorial calculation, implemented in 3 functions
"""
import math


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
    TODO: Make it work
    :param val:
    :return:
    """
    while val != 0:
        val *= val - 1
        val -= 1
    return val


def stdlib_factorial(val: int):
    """
    Use stdlib cmath for factorial
    :param val:
    :return:
    """
    return math.factorial(val)


if __name__ == '__main__':
    print(for_factorial(8))
    print(while_factorial(8))
    print(stdlib_factorial(8))
