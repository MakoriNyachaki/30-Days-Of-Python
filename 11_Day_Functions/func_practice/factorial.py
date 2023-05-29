from __future__ import print_function

"""
Call your function factorial, it takes a whole number
as a parameter and it return a factorial of the number
"""


def factorial(n):
    fact = 1
    for num in range(n):
        num = num + 1
        if num > 0:
            fact *= num
    print(fact)


factorial(5)
