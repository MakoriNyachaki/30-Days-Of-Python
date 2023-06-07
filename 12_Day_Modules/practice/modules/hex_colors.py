from __future__ import print_function
from random import randint, random
import string
import random

"""
Write a function list_of_hexa_colors which returns any number of
hexadecimal colors in an array (six hexadecimal numbers written after #.
Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6
letters of the alphabet, a-f. Check the task 6 for output examples).

Write a function list_of_rgb_colors which returns any number of
RGB colors in an array.

Write a function generate_colors which can generate any number
of hexa or rgb colors.
"""

def main():
    print(list_of_rgb_colors())
    print(list_of_hexa_colors())


def list_of_hexa_colors(no_of_hex_col_codes: int) -> list:
    hexa_codes = []
    letters = 'abcdef'
    for i in range(no_of_hex_col_codes):
        hex_color = ''.join(
            [random.choice(letters + string.digits)
                for n in range(6)
                ]
            )
        new_hex = hexa_codes.append(f'#{hex_color}')
    return hexa_codes



def list_of_rgb_colors(num: int) -> list:
    rgb_lst = []
    for i in range(num):
        color_code = f'{randint(0, 255)},{randint(0, 255)},{randint(0, 255)}'
        new_rgb_lst = rgb_lst.append(f'rgb({color_code})')
    return rgb_lst


if __name__ == '__main__':
    # main()
    pass
