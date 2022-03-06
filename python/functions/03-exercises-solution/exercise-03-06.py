#!/usr/bin/env python3

"""
A recursion example from Problem 3.6.
"""

from math import ceil, floor

# Note that the following two functions can be written using only
# integer arithmetics if the context in `f` is considered.

def g(x):
    """
    Returns the ceiling (the smallest following integer) of `x/2`.
    """
    return ceil(x/2)

def h(x):
    """
    Returns the floor (the largest previous integer) of `x/2+1`.
    """
    return floor(x/2+1)

def f(x):
    """
    Returns :math:`f(x) = \\begin{cases}
            x^2, & x < 9, \\\\
            f(g(x)), & \\text{$x \\ge 9$ is even}, \\\\
            f(h(x+1)), & \\text{otherwise},
        \\end{cases}`
    """

    if x < 9:
        return x ** 2
    if x % 2 == 0:
        return f(g(x))
    return f(h(x+1))

def main():
    x = int(input("x = "))
    while x != 0:
        print("f(" + str(x) + ") =", f(x))
        x = int(input("x = "))
    
main()
