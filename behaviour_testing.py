"""-*- coding: utf-8 -*-"""

temp_val = True

i = 0  # if only python variables could be initialized without any value or could refer to itself on first usage
while temp_val:
    i += 1
    print(i)
    if temp_val and i == 9:
        temp_val = False
        continue
    print("\nnull")
