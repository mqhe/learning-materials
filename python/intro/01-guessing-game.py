#!/usr/bin/env python3

"""
Created on Thu Jan 14 11:21:30 2016

@author: Stefan

This is a game for guessing a random number between 1 and 100. 
It is explained in this Youtube video: 
https://www.youtube.com/watch?v=pofWfJc3Zog

What you read here (and everything that is enclosed by three ")
is a doc-string, a human-readable documentation of your code. 
Everything following a # counts as a comment and is ignored.
It's a good habit (and in this course compulsory!) to always put
a doc-string and lots of MEANINGFUL comments in your code.

If you have managed to open this script in Spyder, you can hit the
[F5] key on your keyboard to execute the script. Watch what happens 
on the right in the 'Console'. You can click into it and enter 
something with your keyboard.
"""

from random import randint # necessary to generate random integer on line 26

print("Guess a number between 1 and 100.")
randomNumber = randint(1,100) # random integer between 1 and 100
trials = 0 # number of trials
    
while True: # keeps looping forever unless a break command appears

    userGuess = input("Your guess: ")    
    userGuess = int(userGuess)
    trials = trials + 1
    
    if userGuess == randomNumber:
        print("Congratulations!")
        print("You guessed correctly after " + str(trials) + " trials.")
        break
    else:
        print("Not correct!")
        if userGuess > randomNumber:
            print("Try a smaller number.")
        else:
            print("Try a larger number.")

