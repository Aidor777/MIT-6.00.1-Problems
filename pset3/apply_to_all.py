# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:14:19 2019

@author: guill
"""

testList = [1, -4, 8, -9]

def absoluteVal(num):
    if num >= 0:
        return num
    else:
        return -num

def power2(num):
    return num*num
    
def sum1(num):
    return num + 1

def times5(num):
    return 5*num

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
applyToEach(testList, power2)
        
print(testList)