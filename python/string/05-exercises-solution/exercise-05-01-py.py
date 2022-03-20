#!/usr/bin/env python3

"""
A (more) Pythonic solution for Problem 1.
"""

def copy_rev(s):
    """
    Returns `s+rev(s)` where `rev(s)` is a reverse of `s`.
    """
    return s + s[::-1]

	
def main():
	s = input("A string:   ")
	print("The result:", copy_rev(s))

main()