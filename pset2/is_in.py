# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:01:30 2019

@author: guill
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    #Base cases
    if aStr == "": #Case when string is empty
        return False
    
    test = aStr[len(aStr)//2] #Get the middle character
    
    if len(aStr) == 1: #Case when string is a simple character
        if char == aStr:
            return True
        else: 
            return False
    elif char == test: #Case when the middle character is actually the same as the tested one
        return True
    
    #Recursion
    if char < test: #Keep the first half
        return isIn(char, aStr[:aStr.index(test)])
    else: #Keep the second half
        return isIn(char, aStr[aStr.index(test)+1:])
    
a = isIn('g', "")
    