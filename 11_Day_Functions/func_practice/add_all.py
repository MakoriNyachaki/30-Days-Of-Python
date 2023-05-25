from __future__ import print_function


def add_all_nums(*nums):
    sum = 0
    for i in nums:
        if int(i):
            sum += i
        else:
            return "Not a number"
    return sum


print(f"Sum is: {add_all_nums(10, 20, 30, 40, 50)}\n")
