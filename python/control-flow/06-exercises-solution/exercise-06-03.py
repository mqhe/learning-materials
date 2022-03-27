#!/usr/bin/env python3

"""
A program that loads a list of integers and prints the first prime in it.
"""

# Since no input method is given for the program, let us use this one a bit.
def load_a_list_of_ints_as_a_string():
    """
    Loads a list integers with a singe call to `input`.
    It is assumed that the list is given in the form `"x1,x2,...,xn"`.
    """
    print("Your list of integers (separate each two numbers with a single comma):")
    data = input()
    if len(data) == 0:
        return []
    return [int(x) for x in data.split(",")]

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

def first_plus_last_prime(L):
    """
    Prints the first prime number in the list `L`.
    """
    # Find the leftmost prime
    found = False
    for left in L:
        if is_prime(left):
            found = True
            break
    if not found:
        # No prime numbers in the list, so we stop the function and return 0.
        return 0

    # Find the rightmost prime
    for right in reversed(L):
        if is_prime(right):
            # We have just found the rightmost prime, so we stop the function,
            # returning the required sum
            return left + right
    # Note: it is impossible to NOT find the rightmost one. That would mean
    # that there are no primes in the list, but in that case the function
    # would have been stopped before (`return 0`).
    # So, the control never reaches this part of the function, as either
    # `return 0` or `return left+right` will be executed.

def main():
	lst = load_a_list_of_ints_as_a_string()
	print("The sum of the first and the last primes in the list is {}.".format(first_plus_last_prime(lst)))

main()