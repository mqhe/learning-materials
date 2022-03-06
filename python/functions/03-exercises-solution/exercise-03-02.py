#!/usr/bin/env python3

"""
A program that compares integer and floating point algorithms
for computing binomial coefficients.
"""

def binom(n, k):
    """
    Returns the binomial coefficient `n` over `k` using
    the integer arithmetics.
    """

    if n < 0 or k < 0 or n < k:
        return 0

    # To reduce the computation, we replace n!/(k!(n-k)!) with
    # the equivalent expression
    # n(n-1)...(n-k+1)/k!
    # Further, this is best done when `k <= n-k` and, since
    # binom(n,k) == binom(n,n-k),
    # we replace `k` with `n-k` when `k > n-k`.

    if k > n-k:
        k = n - k

    res = 1
    for i in range(n-k+1, n+1):
        res *= i
    for i in range(2, k+1):
        res //= i
    return res

def binomf(n, k):
    """
    Returns the binomial coefficient `n` over `k` using
    the floating point arithmetics.
    """

    if n < 0 or k < 0 or n < k:
        return 0

    # To reduce the computation, we replace n!/(k!(n-k)!) with
    # the equivalent expression
    # n(n-1)...(n-k+1)/k!
    # Further, this is best done when `k <= n-k` and, since
    # binom(n,k) == binom(n,n-k),
    # we replace `k` with `n-k` when `k > n-k`.

    if k > n-k:
        k = n - k

    res = 1
    for i in range(n-k+1, n+1):
        res *= i
    for i in range(2, k+1):
        res /= i

    # Removing `int` from the following line would make the function
    # work for all `n` (including the non-integer ones), but in this
    # problem we are comparing two algorithms for integer `n`, so
    # this function has to return integer as well.
    return int(res)

def main():

    n = 100
    k = 50
    
    bnk = binom(n, k)
    bfnk = binomf(n, k)
    
    print("binom: ", bnk)
    print("binomf:", bfnk)
    print("binom-binomf:", bnk - bfnk)
    
main()
    
