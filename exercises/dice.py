#!/usr/bin/env python3.10
"""
Dice sim
"""
import random as rand
from typing import Union


def dice_roll(min_val: int, max_val: int, loops: int = 1) -> Union[None, int, list]:
    """

    :rtype: list, int
    :param min_val:
    :param max_val:
    :param loops:
    :return:
    """
    if loops < 1:
        return
    if loops == 1:
        return rand.randint(min_val, max_val)
    random_values: list = []
    for iteration in range(0, loops):
        random_values.append(rand.randint(min_val, max_val))
    return random_values


occurrences: list = []
totals: list = []
dupes: dict = {}
for i in range(0, 100):
    solver: list = []
    solver_sum: int = 0
    for j in dice_roll(1, 6, 3):
        solver.append(j)
    solver_sum: int = sum(solver)
    if solver_sum in occurrences:
        if solver_sum in dupes.keys():
            dupes[solver_sum] += 1
        else:
            dupes[solver_sum] = 2
    else:
        occurrences.append(solver_sum)
    totals.append(solver_sum)

# Logic is set up bu
for key in dupes.keys():
    print(key / len(dupes.keys()))

print(len(totals))
print(sum(totals) / len(totals))
