#!/usr/bin/env python3

"""
A recursion example from Problem 3.5.
"""

def largest_divisor(x):
    """
    Returns the largest divisor of `x >= 2` that is smaller than `x`.
    If `x` is a prime number, the function returns 1.
    """

    # We start with the largest candidate and go down to the smallest one.
    # The first one we find is the one we want, so we interrupt the function
    # and return the value of the divisor `d`.
    for d in range(x // 2, 2, -1):
        if x % d == 0:
            return d
    return 1

def f(x):
    """
    Returns :math:`f(x) = \\begin{cases}
        f(17 - |x|), & x < 2, \\\\
            f(d), & \\text{$x$ is a composite number and $d$ is its largest divisor such that $d < x$}, \\\\
            x, & \\text{otherwise}.
        \\end{cases}
    """

    if x < 2:
        return f(17 - abs(x))
    d = largest_divisor(x)
    if d > 1:
        return f(d)
    return x

def main():
    x = int(input("x = "))
    while x != 0:
        print("f(" + str(x) + ") =", f(x))
        x = int(input("x = "))
    
main()
