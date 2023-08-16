#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0,)
    if len(tuple_a) < 1 or len(tuple_b) < 1:
        tuple_a = tuple_a + tuple_c
        tuple_b = tuple_b + tuple_c
    return tuple(map(lambda x, y: x + y,tuple_a, tuple_b))
