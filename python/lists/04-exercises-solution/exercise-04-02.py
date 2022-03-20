#!/usr/bin/env python3

"""
A program that loads a list and then creates a new one with the elements
in reversed order, without using Python's built-in functions for reversing
them.
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

def my_reverse(L):
    """
    Returns a new list with the elements of `L` in reversed order.
    """
    # Copy the list `L` to a new list `newL`.
    # Note: this is not good enough if `L` contains more complex objects than
    # just numbers.
    # In exercise-04-04.py we show how is such copying done properly, using
    # Python's mechanisms.
    newL = list()
    for el in L:
        newL.append(el)

    # The rest is the same as it is in exercise-04-01.py
    left = 0  # index of a left element to swap
    right = len(newL) - 1  # index of a right element to swap
    while left < right:
        temp = newL[left]
        newL[left] = newL[right]
        newL[right] = temp
        left += 1
        right -= 1

    # Of course, we need to return the new list
    return newL

def main():
	x = load_a_list_of_ints()
	y = my_reverse(x)
	print("The original list:", x)
	print("A reversed list:  ", y)

main()
