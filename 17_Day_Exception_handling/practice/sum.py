from __future__ import print_function
from typing import Union

"""
Type hints
Handling Exceptions
"""


def main():
    nums = [50.75, 60, 70, 80, 90, 100]
    try:
        sum = get_sum(*nums)
    except UnboundLocalError:
        print("Variable name same as function name")
    else:
        print(f"The sum is {sum}\n")


def get_sum(*args: Union[int, float]) -> Union[int, float]:
    total = 0
    try:
        for arg in args:
            total += arg
    except TypeError:
        print("One of the values not of int or float type")
    else:
        return total


main()
