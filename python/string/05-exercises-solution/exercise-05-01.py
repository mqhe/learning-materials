#!/usr/bin/env python3

"""
A program that takes a string `s` and prints `s+rev(s)` where
`rev(s)` is a reverse of `s`.
"""

def copy_rev(s):
    """
    Returns `s+rev(s)` where `rev(s)` is a reverse of `s`.
    """
    return s + "".join(reversed(s))

def main():
	s = input("A string:   ")
	print("The result:", copy_rev(s))

main()