#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    del my_list[idx]
    # for i in range(len(my_list)):
    # if i != idx:
    # New_list.append(my_list[i])
    return (my_list)
