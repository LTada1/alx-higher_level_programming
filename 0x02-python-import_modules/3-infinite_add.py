#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    add = 0
    if (length == 0):
        print("{}".format(add))
    else:
        j = 1
        while j <= length:
            add += int(argv[j])
            j += 1
        print("{}".format(add))
