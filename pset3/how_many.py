# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:50:47 2019

@author: guill
"""

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    sum = 0
    
    for i in aDict.values(): #Goes through every list
        sum += len(i) #Lenght of said list
    
    return sum

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = 0
    correspKey = "None" #If there is no list in there
    for key in aDict: #Try each entry
        if len(aDict[key]) > biggest: #Lenght of the associated list
            biggest = len(aDict[key])
            correspKey = key
            
    return correspKey
    
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(howMany(animals))

print(biggest(animals))




