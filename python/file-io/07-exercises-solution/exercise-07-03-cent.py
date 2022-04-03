#!/usr/bin/env python3

"""
A solution of Problem 3 with GFM-centered columns.
"""

def line(n, a=None):
    """
    Returns `a`-th line in the table. If `a` is `None`,
    then it returns the header line.
    """
    if a is None:
        # First cell is empty
        res = fmt.format("*")
        # The rest will be as for `a = 1`
        a = 1
        # A header, so it should be followed by a header separator
        hsep = "|".join([":{}:".format("-" * width) for _ in range(n+1)]) + "\n"
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
	width = len(str(n*n))
	fmt = " {:^" + str(width) + "} "

	with open(fname, mode="w", encoding="utf8") as f:
		f.write(line(n))
		for a in range(1, n+1):
			f.write(line(n, a))

main()