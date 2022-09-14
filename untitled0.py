# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:59:13 2022

@author: Ilya
"""
low = 0
high = 100
ans = 0
prompt = ''

print("Please think of a number between 0 and 100!")

while prompt != "c":
    ans = int((low + high)/2)
    print("Is your secret number " + str(ans) + "?")
    print("Enter 'h' to indicate the guess is too high.", end = " ")
    print("Enter 'l' to indicate the guess is too low.", end = " ")
    prompt = input("Enter 'c' to indicate I guessed correctly.")
    if prompt == 'h':
        high = ans
    elif prompt == 'l':
        low = ans
    else:
        if prompt != 'c':
            print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(ans))