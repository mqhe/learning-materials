#!/usr/bin/env python3

"""
A program that loads numbers `n`, `d`, and `r`, and prints maximum digit of `n`
that  gives the reminder `r` when divided by `d`.
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
        The number by which each digit is to be divided.
        If d == 0, an error occurs.
    r : int
        The desired reminder of the division.
        If r < 0 or r >= d, the result will be -1.

    Returns
    -------
    max_digit : int
        The resulting maximum digit or -1 if it doesn't exits.
    """

    n = abs(n)  # We can change `n` because it's just a copy of the function's first argument
    res = -1    # Conveniently, -1 is less than all digits;
                # if it stays the same, no appropriate digit was found, and we just return it
    while n > 0:
        digit = n % 10
        n //= 10
        if digit % d == r and digit > res:
            res = digit
    return res


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
    
