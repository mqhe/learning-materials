#!/usr/bin/env python3

"""
A program that loads integers until it gets a negative number of a zero and
prints the product of all the loaded prime numbers.
"""

def prime(n):
    """
    Returns `True` if `n` is a prime number and `False` otherwise.
    """

    if n < 2:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

def main():
    """
    Loads integers until it gets a negative number or a zero, and then
    prints the product of all the loaded prime numbers. 
    """
    
    res = 1
    
    n = int(input("Type an integer (a non-positive one to quit): "))
    while n > 0:
        if prime(n):
            res *= n
        n = int(input("Type an integer (a non-positive one to quit): "))
    
    if res == 1:
        # Obviously, no primes were loaded, because otherwise
        # the product would be at least 2
        print("No primes were loaded.")
    else:
        print("The product of the loaded primes:", res)
        
main()
    
