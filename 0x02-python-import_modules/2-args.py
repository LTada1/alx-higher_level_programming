#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	""" Print line arguments """
	n = len(argv) - 1
	if n != 0:
		if n == 1:
			print("{} argument:".format(n))
		else:
			print("{} arguments:".format(n))
		j = 1
		while (j <= n):
			print("{}: {}".format(n, argv[j]))
			j += 1
	else:
		print("{} arguments:".format(n))
