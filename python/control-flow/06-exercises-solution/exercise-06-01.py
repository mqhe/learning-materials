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

def print_first_prime(L):
    """
    Prints the first prime number in the list `L`.
    """
    for x in L:
        if is_prime(x):
            print("  The first prime in the list is:", x)
            return  # We're done, so stop the function
    print("  The list contains no primes.")

# There is no real need to use `break` instead of `return`, but here is
# that version of the code as well:
def print_first_prime_with_break(L):
    """
    Prints the first prime number in the list `L`.
    """
    for x in L:
        if is_prime(x):
            print("  The first prime in the list is:", x)
            break  # Without this `break`, the message would get printed for all the primes in `L`
    else:  # This `else` belongs to `for`, NOT `if`!
        print("  The list contains no primes.")

def main():
	lst = load_a_list_of_ints()
	print("The function stopped by a return:")
	print_first_prime(lst)
	print("The function with a loop stopped by a break:")
	print_first_prime_with_break(lst)

main()
