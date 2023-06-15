#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    """print number and list of arguments."""
    j = len(argv) - 1
    if j != 0:
        if j == 1:
            print("{} argument:".format(j))
        else:
            print("{} arguments:".format(j))
        k = 1
        while(k <= j):
            print("{}: {}".format(k, argv[k]))
            k += 1
    else:
        print("{} arguments.".format(j))
