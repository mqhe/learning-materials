#!/usr/bin/env python3

"""
"""

def file2set(fname):
    """
    Returns the set of integers written in the file `fname`, one per a line.
    """
    with open(fname, mode="r", encoding="utf8") as f:
        return { int(line) for line in f }

		
def main():
	fname1 = input("File 1: ")
	fname2 = input("File 2: ")
	set1 = file2set(fname1)
	set2 = file2set(fname2)

	if set1 == set2:
		print('The numbers in files "{}" and "{}" form identical sets of integers.'.format(fname1, fname2))
	elif set1 < set2:
		print('The numbers in file "{}" form a proper subset of those in file "{}".'.format(fname1, fname2))
	elif set1 > set2:
		print('The numbers in file "{}" form a proper subset of those in file "{}".'.format(fname2, fname1))
	else:
		print('The numbers in files "{}" and "{}" are not each other\'s subsets.'.format(fname1, fname2))

main()