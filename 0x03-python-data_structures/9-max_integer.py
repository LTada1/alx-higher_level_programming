#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    maxi = my_list[0]
    if len(my_list) == 0:
        return (None)

    for i in my_list:
        if i > maxi:
            maxi = i

    return (maxi)
