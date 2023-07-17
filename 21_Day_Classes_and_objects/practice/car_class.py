"""
A module implementing the car class
It adds gas, drives for a given distance
checks the amount of gas left in the tank
"""
from __future__ import print_function


class Car:
    # Constructor
    def __init__(self, _consumption, _initialGas=0, _initialMiles=0):
        self._consumption = _consumption
        self._remainingGas = _initialGas
        self._milesDriven = _initialMiles
        self._distanceCovered = 0

    # Add gas adds gas to the car's tank
    # @param amount Amount of gas to add
    def addGas(self, amount):
        self._remainingGas += amount

    # drive for a given distance in miles
    # @param distance Distance to drive
    def drive(self, distance):
        self._milesDriven += distance

    # check gas checks for the gas remaining in the tank
    def checkGas(self):
        spentGas = self._remainingGas - self._milesDriven / self._consumption
        return spentGas

    # Get miles driven distance covered
    # @param distance distance covered
    def getMilesDriven(self):
        return self._milesDriven
