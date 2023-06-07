from __future__ import print_function
from random import randint

"""
Write a function named rgb_color_gen. It will generate rgb colors
(3 values ranging from 0 to 255 each).
    print(rgb_color_gen())
    # rgb(125,244,255) - the output should be in this form
"""


def main():
    print(rgb_color_gen())


def rgb_color_gen():
    return f'rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})'


if __name__ == '__main__':
    main()
