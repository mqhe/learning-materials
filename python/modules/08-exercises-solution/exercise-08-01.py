#!/usr/bin/env python3

"""
A module for searching for the prime numbers among
the digit-wise permutations of a given number.
"""

from itertools import permutations

def is_prime(n):
    """
    Returns `True` if `n` is prime, and `False` otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def has_prime_perm(n):
    """
    Returns `True` if any digit-wise permutation of `n` forms a prime number.
    """
    if n < 2:
        return False
    for perm in permutations(str(n)):
        if is_prime(int("".join(perm))):
            return True

def has_only_prime_perms(n):
    """
    Returns `True` if all digit-wise permutation of `n` form prime numbers.
    """
    if n < 2:
        return False
    return all(is_prime(int("".join(perm))) for perm in permutations(str(n)))

def prime_perms(n):
    """
    Returns a generator for a list of prime permutations of `n`.
    """
    if n < 2:
        return
    for perm in permutations(str(n)):
        num = int("".join(perm))
        if is_prime(num):
            yield num

if __name__ == "__main__":
    n = int(input("n = "))
    if has_prime_perm(n):
        print("The prime permutations of {} are:\n{}".format(n, list(prime_perms(n))))
        if has_only_prime_perms(n):
            print("Actually, all of the permutations of {} are prime numbers.")
    else:
        print("The number {} has no prime permutations.".format(n))

