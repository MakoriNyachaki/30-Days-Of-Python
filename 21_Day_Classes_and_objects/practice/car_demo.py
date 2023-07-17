"""
Demonstarting the car class
"""

from __future__ import print_function
from car_class import Car

myCar = Car(25)
myCar.addGas(20)
myCar.drive(100)
myCar.drive(200)
myCar.addGas(5)

print(myCar.checkGas())
