from __future__ import print_function

"""
Declare a function named reverse_list. It takes an array as a parameter and
it returns the reverse of the array (use loops).
"""


def reverse_list(ls):
    for item in ls:
        item = ls[-1::-1]
    return item


print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
