# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:30:22 2019

@author: guill
"""

def genPrimes():
    
    listPrimes = [2] # start with the base case of the first prime number
    x = 2
    sequence = '2'
    
    while True: # allows to call the function infinitely as long as __next__() is called
       
        test = True # assume the number is prime, then we will test this
        for p in listPrimes:
            
            if (x % p) == 0 and x != 2: # a number that is not prime
                
                x += 1
                test = False # the number is not prime and will later not be added
                break
            
        if x == 2: # implement the first case for x = 2
            
            test = False
            x += 1
            yield sequence
        
        if test == True: #add the new prime number to the list and the sequence and yield the sequence at the time
            
            listPrimes.append(x)
            sequence = sequence + ', ' + str(x)
            yield sequence
            x += 1