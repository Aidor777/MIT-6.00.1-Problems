# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:33:29 2019

@author: guill
"""

s = "abcbcd"
order = ""
tempstring = ""

for i in range(len(s)): #test for every letter in sequence
    for j in range(i, len(s)-1): #
        if s[j] > s[j+1]:
            break #go to next letter if not in alphabetical order
        else:
            tempstring = s[i:j+2]
            
        if len(tempstring) > len(order): #only keep the longest substring 
            order = tempstring

print("Longest substring in alphabetical order is: ", order)