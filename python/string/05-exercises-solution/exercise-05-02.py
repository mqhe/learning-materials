#!/usr/bin/env python3

"""
A program that takes a string `s` and prints it expanded up to a given
length with and without slicing it at the end.
"""

def copy_to_len_whole(s, l):
    """
    Returns the maximum length string made of copies of `s`
    (only the whole `s`, no slicing) with the length at most `l`.
    """
    res = ""
    while len(res + s) <= l:
        res += s
    return res

def copy_to_len_sliced(s, l):
    """
    Returns the maximum length string made of copies of `s`
    with the length exactly `l`; if the length of `s` doesn't match,
    it ends with the beginning slice of `s`.
    """
    res = ""
    while len(res) <= l:
        res += s
    # Here: len(res) >= l, so we return the beginning slice
    return res[:l]

def main():
	s = input("A string: ")
	l = int(input("The desired length: "))
	print("copy_to_len_whole:", copy_to_len_whole(s, l))
	print("copy_to_len_whole:", copy_to_len_sliced(s, l))

main()