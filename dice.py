#!/user/bin/env python3.10
"""
Dice sim
"""
import random as rand

def dice_roll(min_val, max_val, loops: int = 0):

    if loops == 0:
        return rand.randint(min, max)
