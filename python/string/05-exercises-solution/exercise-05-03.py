#!/usr/bin/env python3

"""
A program that loads a string and prints its left and right fading copies.
"""

def fade_copies_left(s):
    """
    Returns the string made by concatenating `s` with its left slices of
    decreasing sizes, i.e., with the `s` without the last character, then
    with `s` without the last two characters, etc.
    """
    res = ""
    for k in reversed(range(len(s))):
        res += s[:k+1]
    return res

def fade_copies_right(s):
    """
    Returns the string made by concatenating `s` with its right slices of
    decreasing sizes, i.e., with the `s` without the first character, then
    with `s` without the first two characters, etc.
    """
    res = ""
    for k in range(len(s)):
        res += s[k:]
    return res

def main():
	s = input("A string: ")
	print("Left fade: ", fade_copies_left(s))
	print("Right fade:", fade_copies_right(s))

main()