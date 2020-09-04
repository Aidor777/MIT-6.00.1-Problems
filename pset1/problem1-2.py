# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:27:33 2019

@author: guill
"""

s = "bobsdaljfbobwroquvsdjkgfbobwpfsaobob"
count = 0

for temp in range(len(s)):
    if s[temp: temp+3] == "bob":
        count += 1
        
print("Number of times bob occurs is: ", count)