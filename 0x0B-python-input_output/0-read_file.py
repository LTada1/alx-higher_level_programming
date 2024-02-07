#!/usr/bin/python3
""" Function for reading files"""

def read_file(filename=""):
	""" Reads file content """
	with open(filename, encoding="utf-8") as f:
		content = f.read()
		print(f"{content}")
