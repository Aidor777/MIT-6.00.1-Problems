# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:44:03 2019

@author: guill
"""

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

list = [1,6,2,9,4,12,0,8]    
modSwapSort(list)        
    
    