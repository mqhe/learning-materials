#!/usr/bin/env python3

"""
A program that sorts a list without using Python's built-in functions for sorting them.
"""

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
    Sorts the list `L`.
    """
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

def main():
	x = load_a_list_of_ints()
	print("Before sorting:", x)
	my_sort(x)
	print("After sorting: ", x)

main()