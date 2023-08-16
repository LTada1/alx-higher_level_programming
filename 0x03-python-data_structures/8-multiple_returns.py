#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    if len(sentence) < 1:
        return (None)
    return (len(sentence), sentence[0])
