#!/usr/bin/env python3

"""
A Pythonic solution for Problem 6.4.
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
    # We use the fact that `max` raises a ValueError exception
    # when the given set of values is empty.
    # Note that the message is somewhat wrong for the occasion
    # ("max() arg is an empty sequence"), but it isn't far from
    # what we need (we do need a maximum digit that doesn't exist).
    return max(digit for digit in digits if digit % d == r)

def main():
	n = int(input("n = "))
	d = int(input("d = "))
	r = int(input("r = "))

	try:
		print("A required digit:", max_digit(n, d, r))
	except ValueError:
		print("There are no such digits.")

main()