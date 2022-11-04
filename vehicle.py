# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:08:30 2022

@author: ishde
"""

class Vehicle:
    """
    Vehicle models a device that can be used to travel
    """
    def __init__(self, distance_traveled=0, unit='miles'):
        print(f"__init__ from Vehicle with distance_traveled: {distance_traveled} and {unit}")
        self.distance_traveled = distance_traveled
        self.unit = unit
        
    def description(self):
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"