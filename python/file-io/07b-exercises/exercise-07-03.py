#!/usr/bin/env python3

"""
A program that loads an integer `n` and a file name, and then
creates a text file with that name containing
the [multiplication table](http://en.wikipedia.org/wiki/Multiplication_table)
for all numbers between 1 and `abs(n)` (including both of them).
"""

def line(n, a=None):
    """
    Returns `a`-th line in the table. If `a` is `None`,
    then it returns the header line.
    """
    
    width = len(str(n*n))
    fmt = " {:^" + str(width) + "} "
    
    if a is None:
        # First cell is empty
        res = fmt.format("*")
        # The rest will be as for `a = 1`
        a = 1
        # A header, so it should be followed by a header separator
        hsep = "|".join(["-" * (width+2) for _ in range(n+1)]) + "\n"
    else:
        # Add the first cell in this row
        res = fmt.format(a)
        # Not a header, so no header separator
        hsep = ""
    # Add the remaining cells
    for b in range(1, n+1):
        res += "|" + fmt.format(a * b)
    return res + "\n" + hsep

def main():
	n = abs(int(input("n = ")))
	fname = input("File name: ")
	

	with open(fname, mode="w", encoding="utf8") as f:
		f.write(line(n))
		for a in range(1, n+1):
			f.write(line(n, a))

main()