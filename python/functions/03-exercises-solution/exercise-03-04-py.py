#!/usr/bin/env python3

"""
A Pythonic solution for Problem 3.4.
"""

def rich(n):
    """
    Returns `True` if `n` is "rich" (i.e., `abs(n)` is smaller than
    the sum of its divisors excluding itself) and `False` otherwise.
    """
    n = abs(n)
    return n < sum(k for k in range(1, n) if n % k == 0)

def main():
    
    k = 50
    
    print("The rich numbers between 1 and {} (inclusive): {}".format(k, ", ".join(str(n) for n in range(1, k+1) if rich(n))))

main()