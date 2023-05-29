from __future__ import print_function

"""
Declare a function named sum_of_odds. It takes
a number parameter and it adds all the odd numbers in that range.
"""


def sum_of_odds(n):
    sumo = 0
    if n % 2 == 1:
        sumo += n
    for num in range(n):
        if num % 2 == 1:
            sumo += num
    return sumo


print(sum_of_odds(10))
