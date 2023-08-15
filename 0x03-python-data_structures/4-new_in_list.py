#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if idx < 0:
        return (my_list)
    if idx > (len(my_list)-1):
        return (my_list)
    copy_list[idx] = element
    return (copy_list)
