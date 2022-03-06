#!/usr/bin/env python3

"""
A program that loads a natural number `k` and prints all the "rich" numbers between 1 and `k` (inclusive).
"""

def rich(n):
    """
    Returns `True` if `n` is "rich" (i.e., `abs(n)` is smaller than
    the sum of its divisors excluding itself) and `False` otherwise.
    """

    n = abs(n)
    sum_of_divisors = 0

    for k in range(1, n):
        if n % k == 0:
            sum_of_divisors += k

    return n < sum_of_divisors

def main():

    k = 50
    
    print("The rich numbers between 1 and", k, "(inclusive):")
    for n in range(1, k+1):
        if rich(n):
            print(n)

main()