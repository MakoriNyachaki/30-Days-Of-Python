from __future__ import print_function

"""
Declare a function named evens_and_odds . It takes a positive integer
as parameter and it counts number of evens and odds in the number.
"""


def evens_and_odds(n):
    count_even = 0
    count_odd = 0
    if n % 2 == 1:
        count_odd += 1
    else:
        count_even += 1
    for num in range(n):
        if num % 2 == 1:
            count_odd += 1
        else:
            count_even += 1
    return f"Odd numbers are: {count_odd}\nEven numbers are: {count_even}"


print(evens_and_odds(1000))
# The number of odds are 50.
# The number of evens are 51.
