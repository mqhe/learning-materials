#!/usr/bin/env python3

"""
A (more) Pythonic/mathematical solution for Problem 2.
"""

def copy_to_len_whole(s, l):
    """
    Returns the maximum length string made of copies of `s`
    (only the whole `s`, no slicing) with the length at most `l`.
    """
    return s * (l // len(s))

def copy_to_len_sliced(s, l):
    """
    Returns the maximum length string made of copies of `s`
    with the length exactly `l`; if the length of `s` doesn't match,
    it ends with the beginning slice of `s`.
    """
    return s * (l // len(s)) + s[:l%len(s)]

def main():
	s = input("A string: ")
	l = int(input("The desired length: "))
	print("copy_to_len_whole:", copy_to_len_whole(s, l))
	print("copy_to_len_whole:", copy_to_len_sliced(s, l))

main()