#!/usr/bin/env python3

"""
A program that loads a list of integers and prints the first prime in it.
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

def is_prime(n):
    """
    Returns `True` if `n` is prime, and `False` otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime(L):
    """
    Prints the first prime number in the list `L`.
    """
    for x in L:
        if is_prime(x):
            return x  # We're done, so stop the function
    # No prime numbers in the list, so we raise an exception.
    # We choose `ValueError`, but we could've made our own as well.
    raise ValueError("the list contains no prime numbers")

def main():
	lst = load_a_list_of_ints()
	try:
		print("The first prime in the list is {}.".format(first_prime(lst)))
	except ValueError:
		print("The list contains no primes.")

main()