from __future__ import print_function

"""
Declare a function named sum_of_numbers. It takes a number
parameter and it adds all the numbers in that range.
"""


def sum_of_numbers(n):
    total = 0
    # range is exclusive of the last item in the range, therefore;
    total += n
    for num in range(n):
        total += num
    return total


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050
