#!/usr/bin/env python3

"""
A program that loads a text, line by line, until it loads an empty line.
It then prints how many Python keywords were in it.
It is assumed that all the words are separated by one or more spaces.
"""

from keyword import iskeyword

cnt = 0
words = dict()
while True:
    line = input()
    if line == "":
        break
    for word in line.split(" "):
        # If there are consecutive spaces, some words will be empty.
        # This is not a problem, because "" is not a Python keyword.
        if iskeyword(word):
            cnt += 1
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
print("Total number of keywords:", cnt)
if words:
    for word,wcnt in words.items():
        print('Keyword "{}" has appeared {} times.'.format(word, wcnt))

