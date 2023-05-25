from __future__ import print_function


def convert_celsius_to_fahrenheit(c):
    return (((c * 9)/5) + 32)


c = float(input("Enter your temp in degrees celsious: "))
print(f"Your temp is: {convert_celsius_to_fahrenheit(c)} F\n")
