from __future__ import print_function
from typing import Union

"""
Type hints
Handling Exceptions
"""


def sum(*args: Union[int, float]) -> Union[int, float]:
    total = 0
    for arg in args:
        total += arg
    return total


try:
    nums = [50.75, 60, 70, 80, 90, 100]
    sum = sum(*nums)
    print(f'The sum is {sum}\n')

except TypeError as typee:
    print(f'The error is\n{typee}\n')
except ValueError as error:
    print(f'The error is\n{error}\n')
except SyntaxError as syntax:
    print(f'Invalid syntax. Check on your syntax\n')
