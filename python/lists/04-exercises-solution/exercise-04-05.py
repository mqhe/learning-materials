#!/usr/bin/env python3

"""
A program that loads a sorted (this is not checked!) list of integers and
an additional integer, and checks if that one is a member of the list,
using the binary search algorithm.
"""

def load_a_list_of_ints():
    """
    Loads a list of integers by first asking for its length.
    """
    L = list()
    n = int(input("The number of list elements: "))
    print("Please input your numbers in the sorted order.")
    for k in range(n):
        L.append(int(input(str(k+1) + ". element: ")))
    return L

def search(L, el):
    """
    Returns the index of `el` in `L` if it exists, or `None` otherwise.
    """
    left = 0
    right = len(x)-1

    while right >= left:
        mid = (left + right) // 2
        if L[mid] == el:
            return mid
        if L[mid] < el:
            left = mid + 1
        else:
            right = mid - 1
    return None

	
def main():
	#x = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43]   
	x = load_a_list_of_ints() # comment out for faster testing
	el = int(input("Which number are you interested in? "))

	idx = search(x, el)
	if idx is None:
		print("The number " + str(el) + " does not exist in the list.")
	else:
		print("Index of " + str(el) + " in the list:", idx)

main()