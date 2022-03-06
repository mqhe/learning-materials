#!/usr/bin/env python3

"""
A Pythonic solution for Problem 3.1.
"""

def max_digit(n, d=1, r=0):
    """
    Return the the maximum digit of `n` that gives the reminder `r`
    when divided by `d`, or -1 if such a digit does not exist.

    Parameters
    ----------
    n : int
        A number whose sum is computed.
    d : int
        The number by which each digit is to be devided.
        If d == 0, an error occurs.
    r : int
        The desired reminder of the division.
        If r < 0 or r >= d, the result will be -1.

    Returns
    -------
    max_digit : int
        The resulting maximum digit or -1 if it doesn't exits.
    """

    digits = (int(digit) for digit in str(abs(n)))
    try:
        return max(digit for digit in digits if digit % d == r)
    except ValueError:
        return -1

def main():
    n = 1234
    d = 2
    r = 1
    
    md = max_digit(n, d, r)
    
    if md >= 0:
        print("A required digit:", md)
    else:
        print("There are no such digits.")
    
main()