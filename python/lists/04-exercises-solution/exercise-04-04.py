#!/usr/bin/env python3

"""
A program that loads a list and then creates a new one with the elements
in sorted order, without using Python's built-in functions for sorting
them.
"""

from copy import deepcopy

def load_a_list_of_ints():
    """
    Loads a list of integers by first asking for its length.
    """
    L = list()
    n = int(input("The number of list elements: "))
    for k in range(n):
        L.append(int(input(str(k+1) + ". element: ")))
    return L

def my_sort(L):
    """
    Returns a new list with the elements of `L` in sorted order.
    """
    # Create a new list and save it in the same variable as the old one.
    # Notice that, after this line, the old list is no longer available
    # in this function, because `L` now references to the new list.
    # However, it is still in the memory, and can be accessed through
    # the variable `L` in the main part of the program.
    L = deepcopy(L)

    # The rest is the same as it is in exercise-04-03.py
    n = len(L)
    for left in range(n-1):
        right = left  # assume that this one is the minimum; check all the others
        for k in range(left+1, n):
            if L[k] < L[right]:
                right = k
        if right > left:
            tmp = L[left]
            L[left] = L[right]
            L[right] = tmp

    # Of course, we need to return the new list
    return L

def main():
	x = load_a_list_of_ints()
	y = my_sort(x)
	print("The original list:", x)
	print("A sorted list:    ", y)

main()
