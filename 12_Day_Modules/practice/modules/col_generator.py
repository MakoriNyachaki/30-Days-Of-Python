from __future__ import print_function
from hex_colors import list_of_hexa_colors, list_of_rgb_colors
"""
Write a function generate_colors which can generate any number of hexa or rgb colors.

       generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
       generate_colors('hexa', 1) # ['#b334ef']
       generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
       generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""

def main():
    print(generate_colors('hexA', 4))
    print(generate_colors('hexa', 3)) 
    print(generate_colors('hexa', 1))
    print(generate_colors('rgb', 3)) 
    print(generate_colors('rgb', 1))


def generate_colors(code_type: str, number: int) -> list:
    if code_type.lower() == 'hexa':
        return  list_of_hexa_colors(number)
    elif code_type.lower() == 'rgb':
        return list_of_rgb_colors(number)
    else:
        return f'{code_type} is not a color code type! Enter \'hexa\' or \'rgb\''

if __name__ == '__main__':
    main()
