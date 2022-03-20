#!/usr/bin/env python3

"""
A program that loads a string and prints its second word.
"""

def second_word(s):
    """
    Returns the second word in `s`.
    """
    last = len(s)-1
    start = 0

    # Find the left-most space
    while start <= last and s[start] != " ":
        start += 1
    # Now, start == last+1 or s[start] == " "
    if start > last:
        # There is no second word
        return ""

    # Now, s[start] == " "; let us find the first non-space,
    # which is the beginning of the second word
    while start <= last and s[start] == " ":
        start += 1
    if start > last:
        # There is no second word
        return ""

    # Now, `start` is the index of the first character in the second word.
    # Let us find the next space (which is right after the end of the word).
    end = start
    while end <= last and s[end] != " ":
        end += 1
    # Now, `end` is either the index of the first space after the word,
    # or the first index after the end of the string. In both cases,
    # we need characters `start`, `start+1`,..., `end-1` (bot not `end`!).
    return s[start:end]

def main():
	s = input("A string: ")
	print("Second word: \"{}\"".format(second_word(s)))

main()