#!/usr/bin/env python3

"""
A program that loads a list of strings and prints it sorted by its elements' last words.
"""

def load_a_list_of_strs():
    """
    Loads a list of strings by first asking for its length.
    """
    L = list()
    n = int(input("The number of list elements: "))
    for k in range(n):
        L.append(input(str(k+1) + ". string: "))
    return L

def last_word(s):
    """
    Returns the last word in `s`.
    """
    k = len(s)
    # Find the first `k` after the right-most space,
    # while being careful not to "exit" the list (k > 0).
    while k > 0 and s[k-1] != " ":
        k -= 1
    return s[k:]

	
def main():
	# For testing purposes:
	#s = input("A string: ")
	#print("Last word: \"{}\"".format(last_word(s)))

	L = load_a_list_of_strs()
	L.sort(key=last_word)
	print("Sorted:")
	for s in L:
		print("  {}".format(s))

main()