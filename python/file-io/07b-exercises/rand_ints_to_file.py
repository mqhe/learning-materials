#!/usr/bin/env python3

"""
A program that creates a text file with random integers in a given range,
used to create test files for Problem 1.
"""

from random import randint, shuffle
from sys import exit

def input_int(prompt, fr=None, to=None):
    """
    Inputs and returns an integer between `fr` and `to`, if they are given.
    """
    while True:
        try:
            num = int(input(prompt))
            if fr is not None and num < fr:
                continue
            if to is not None and num > to:
                continue
            break
        except ValueError:
            pass
    return num

def main():
	while True:
		try:
			fname = input("File name: ")
			with open(fname, mode="w", encoding="utf8") as f:
				n = input_int("Number of elements: ", 1)
				fr = input_int("Minimum random number: ")
				to = input_int("Maximum random number: ")
				nums = [str(randint(fr, to)) for _ in range(n)]
				try:
					f.write("\n".join(nums))
				except Exception as e:
					print("Error:", e)
					exit(1)
			break
		except Exception:
			print("Invalid file name.")

	while True:
		try:
			fname = input("Shuffled file name (empty for none): ")
			if fname == "":
				exit(0)
			shuffle(nums)
			with open(fname, mode="w", encoding="utf8") as f:
				try:
					f.write("\n".join(nums))
				except Exception as e:
					print("Error:", e)
					exit(1)
			break
		except Exception:
			print("Invalid file name.")

main()