# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:12:08 2022

@author: ishde
"""

from boat import Boat
from car import Car

class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles'):
        super().__init__(engine, tires, distance_traveled, unit)
        self.boat_type = 'motor'
        
    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)

water_car = AmphibiousVehicle('4 cylinder')
water_car.description()

print(water_car.description())

print(AmphibiousVehicle.__mro__)


##Better Coding

class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles'):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit)
        self.boat_type = 'motor'
        
water_car = AmphibiousVehicle('4 cylinder')
water_car.description()

print(water_car.description())

water_car.voyage

water_car.drive

water_car.travel