#!/usr/bin/env python3
# 5-no_c.py

def no_c(my_string):

    """remove c and C from string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
    # string = ''
    # for i in my_string:
    # if i == 'c' or i == 'C':
    # continue
    # string += i
    # return (string)
