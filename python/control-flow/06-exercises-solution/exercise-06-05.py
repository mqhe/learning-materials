#!/usr/bin/env python3

"""
Get the `k`-th left or right digit from a number.
"""

class WrongArgumentsError(ValueError):
    # We could have used `Exception` instead of `ValueError` and
    # the program would work just as fine. The reason we use `ValueError`
    # is to make it more clear that this error IS related to wrong values
    """
    An error which occurs when the arguments are not properly given.
    """
    pass

def get_len(n):
    """
    Returns the length of a natural number `n`.
    """
    res = 0
    while n > 0:
        res += 1
        n //= 10
    return res

def get_digit(n, *, left=None, right=None):
    """
    Returns either the `left`-th digit of `n` from the left or
    the `right`-th digit of `n` from the right (but not both!).
    """
    n = abs(n)
    # Neither left nor right were given
    if left is None and right is None:
        raise WrongArgumentsError("missing either 'left' or 'right' argument")
    # Left was given
    if left is not None:
        # Both were given
        if right is not None:
            raise WrongArgumentsError("only one of the 'left' and 'right' arguments may be given")
        # The digit doesn't exist
        if left > get_len(n):
            raise ValueError("the {}. digit from the left does not exist".format(left))
        # Get the `left`-th digit from the left
        for _ in range(get_len(n) - left):
            n //= 10
        return n % 10
    # Only right is given
    for _ in range(right - 1):
        n //= 10
    return n % 10

	
def main():
	n = int(input("n = "))
	k = int(input("k = "))

	try:
		print("The {}. digit from the left:  {}".format(k, get_digit(n, left=k)))
	except ValueError as e:
		print("{}.".format(str(e).capitalize()))

	print("The {}. digit from the right: {}".format(k, get_digit(n, right=k)))

	try:
		print(str(k) + ". digit from both sides:", get_digit(n, left=k, right=k))
	except WrongArgumentsError:
		print("Error giving both 'left' and 'right' arguments.")

	try:
		print(str(k) + ". digit from no sides:  ", get_digit(n))
	except WrongArgumentsError:
		print("Error giving neither 'left' nor 'right' argument.")

main()