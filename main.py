# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def for_factorial(val: int):
    for i in range(val-1, 1, -1):
        print(val)
        val = val * i
    return val

#def


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(for_factorial(6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
