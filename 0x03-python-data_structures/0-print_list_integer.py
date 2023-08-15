#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    lap = my_list[:]

    for i in lap:
        prinit("{:d}".format(i))
