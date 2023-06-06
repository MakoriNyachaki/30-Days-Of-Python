from __future__ import print_function

"""
A program that accepts and returns only an integer value
It keeps prompting for an integer value till it is provided
"""


def main():
    x = get_int("What is x? ")
    print(f"X is {x}")


def get_int(int_val):
    while True:
        try:
            return int(input(int_val))
        except ValueError:
            print("X is not an integer")


main()
