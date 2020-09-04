# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:57:57 2019

@author: guill
"""

print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low+high)//2

while (high-low)>=1: # implement bisection search
    print ("Is your secret number", guess, "?")
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if check == "h":
        high = guess
        guess = (low+high)//2
    elif check == "l":
        low = guess
        guess = (low+high)//2
    elif check == "c":
        print("Game over. Your secret number was:", guess)
        break
    else:
        print("Sorry, I did not understand your input.")