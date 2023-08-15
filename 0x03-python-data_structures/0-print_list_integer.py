#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    pat = my_list[:]

    for i in range(len(pat)):
        print("{:d}".format(pat[i]))
