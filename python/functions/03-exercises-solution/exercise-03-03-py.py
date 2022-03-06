#!/usr/bin/env python3

"""
A Pythonic solution for Problem 3.3.
"""

def prime(n):
    """
    Returns `True` if `n` is a prime number and `False` otherwise.
    """

    return n >= 2 and all(n % k for k in range(2, n))


def main():
    """
    Loads integers until it gets a negative number or a zero, and then
    prints the product of all the loaded prime numbers. 
    """
    res = 1
    
    while True:
        n = int(input("Type an integer (a non-positive one to quit): "))
        if n <= 0:
            break
        if prime(n):
            res *= n
    
    if res == 1:
        # Obviously, no primes were loaded, because otherwise
        # the product would be at least 2
        print("No primes were loaded.")
    else:
        print("The product of the loaded primes:", res)
    
main()