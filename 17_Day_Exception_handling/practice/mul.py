from __future__ import print_function
from typing import Union
from functools import partial
import sys

"""
Handling exceptions
Type hints
Partial functions
"""
# Type hint alias

number = Union[float, int]

"""
multiplies a number with an infinite number of values
"""


def multiply(x: number, *args: number) -> number:
    result = x
    for arg in args:
        result *= arg
    return result


try:
    x: number = input("Enter the value of the constant: ")

    y = int(input("How many values do you want to multiply? "))

# Create a list of values you want to multiply with your constant
    values = []

    for num in range(y):
        try:
            val: number = float(input('Enter a value: '))
            # if isinstance(val, (int, float)):
            values.append(val)
        except TypeError:
            print("Not a number or float")
    print(values)
except TypeError:
    pass
# Implementing our partial functin

mul = partial(multiply, 5)
res = mul(*values)

print(res)
