# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:49:43 2019

@author: guill
"""

import math

def polysum(n, s):
    """
    Int n, float or int s
    """
    area = (0.25*n*(s**2))/math.tan(math.pi/n)
    perimeter = n*s
    return round(area + perimeter**2, 4)

a = polysum(3, 5)