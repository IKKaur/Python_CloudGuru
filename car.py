# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:08:51 2022

@author: ishde
##CHAPTER 3
"""

from vehicle import Vehicle

class Car(Vehicle):
    default_tire = 'tire'
    
    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles', **kwargs):
        print(f"__init__ from Car with distance_traveled: {distance_traveled} and {unit}")
        super().__init__(distance_traveled=distance_traveled, unit=unit)
        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tired = tires
        self.engine = engine
        
    def drive(self, distance):
        self.distance_traveled += distance
