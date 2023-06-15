#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    j = len(argv) - 1
    if (j != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    val = argv[2]
    if not (val == '+' or val == '-' or val == '*' or val == '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if (val == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (val == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (val == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
