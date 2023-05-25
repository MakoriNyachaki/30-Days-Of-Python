from __future__ import print_function
import math


def solve_quadratic_eqn(a=1, b=1, c=0):
    """
    The function gonna solve the values of x in the following
    quadratic expression:
    ax² + bx + c = 0.
    x has two values at the end
    It is found by adding or subtracting the value of -b to the value
    of the square root of b squared substracting the value of 4ac
    and finally dividing the result by the value of 2a.
    Returns the values of x
    """
    p = b ** 2
    q = 4 * a * c
    diff = p - q
    if diff > 0:
        root = math.sqrt(root)
        return (f"of x is {(-b + (root)) / (2 * a)} or {(-b - (root)) / (2 * a)}")
    else:
        return (f"{p - q} is less than 0, thus cannot find its square root."
                " Equation cannot be solved!")


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(f"The value {solve_quadratic_eqn(c = c, b = b, a = a)}\n")
