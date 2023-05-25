from __future__ import print_function
import math


def area_of_circle(r):
    return (math.pi * (r ** 2))


r = int(input("Radius: "))
print(f"Area of circle with radius {r} is {area_of_circle(r)} sq. units\n")
