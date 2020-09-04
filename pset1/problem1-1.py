# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:24:59 2019

@author: guill
"""

s = "sdaljfbobwroquvsdjkgfbobwpfsao"
count = 0

for temp in range(len(s)):
    if s[temp] == "a" or s[temp] == "e" or s[temp] == "i" or s[temp] == "o" or s[temp] == "u":
        count += 1
        
print("Number of vowels: ", count)