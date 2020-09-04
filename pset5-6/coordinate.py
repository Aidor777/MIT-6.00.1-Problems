# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:35:17 2019

@author: guill
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        # Assert if we have two instances of the same type
        assert type(self) == type(other)
        # Assess if two points have the same coordinates
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False
        
    def __repr__(self):
        return "Coordinate(" + str(self.x) + ", " + str(self.y) + ")"
        
        
        
        
        
        
        
        
        
        
        
        
        