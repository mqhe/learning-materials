#!/usr/bin/env python3

"""
A program that reverses a list without using Python's built-in functions for reversing them.
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
    Reverses the list `L`.
    """
    left = 0  # index of a left element to swap
    right = len(L) - 1  # index of a right element to swap
    while left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1

def main():
	x = load_a_list_of_ints()
	print("Before reversing:", x)
	my_reverse(x)
	print("After reversing: ", x)

main()