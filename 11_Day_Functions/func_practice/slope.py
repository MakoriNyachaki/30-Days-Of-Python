from __future__ import print_function


def calculate_slope(x1=1, x2=2, y1=1, y2=2):
    """
    Finds the slope of a straight line
    The slope is found by the change in the y-co-ordinates
    divided by the change in the x-coordinates
    Returns the slope
    """
    return ((y2 - y1) / (x2 - x1))


# Enter the values of the coordinates
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

print(f"The slope is: {calculate_slope(x1 = x1, y1 = y1, x2 = x2, y2 = y2)}\n")
