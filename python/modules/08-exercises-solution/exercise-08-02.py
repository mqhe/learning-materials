#!/usr/bin/env python3

"""
A program to detect an average number of swaps of the selection sort of a list of length n with a given sample size with and without repeating elements.
"""

from random import randrange, shuffle

def gen_rand_list(n, distinct=False):
    """
    Returns a random list of numbers from 0 to `n-1`.
    If `distinct == True`, all the elements of the list are distinct,
    i.e., the list is a random permutation of `list(range(n))`.
    """
    if distinct:
        L = list(range(n))
        shuffle(L)
        return L
    else:
        return [randrange(n) for _ in range(n)]

def my_sort(L):
    """
    Sorts `L` using the selection sort algorithm and
    returns the number of performed swaps.
    This function is a slight modification of `my_sort` from "exercise-04-03.py".
    """
    res = 0
    n = len(L)
    for left in range(n-1):
        right = left  # assume that this one is the minimum; check all the others
        for k in range(left+1, n):
            if L[k] < L[right]:
                right = k
        if right > left:
            res += 1
            tmp = L[left]
            L[left] = L[right]
            L[right] = tmp
    return res

n = int(input("List length: "))
sample_size = int(input("Sample size: "))
swaps_all = 0
swaps_distinct = 0

# This next `print` and the one in the loop are for
# those who want to know more and are not considered
# a part of the standard solution.
# The trick is simple: character "\r" is a carriage return,
# which returns the cursor to the beginning of the line:
# http://en.wikipedia.org/wiki/Carriage_return
# `end=""` prevents `print` from appending its usual "\n".
# The display should be nicely seen for `n=100` and `sample_size = 10000`.
print("Tested samples: 0\r", end="")
for k in range(sample_size):
    swaps_all += my_sort(gen_rand_list(n))
    swaps_distinct += my_sort(gen_rand_list(n, True))
    if k % 100 == 0:
        print("Tested samples: {}\r".format(k), end="")

print("Average number of swaps:")
print("    For all the lists: {:.3f}".format(swaps_all / sample_size))
print("    For the lists with only distinct elements: {:.3f}".format(swaps_distinct / sample_size))

