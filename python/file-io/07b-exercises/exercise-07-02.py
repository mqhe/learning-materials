#!/usr/bin/env python3

"""
A program that loads a name of a text file and reverses the order of its lines.
"""

def main():
	fname = input("File name: ")

	with open(fname, mode="r", encoding="utf8") as f:
		lines = [line for line in f]
	with open(fname, mode="w", encoding="utf8") as f:
		f.write("".join(reversed(lines)))

main()