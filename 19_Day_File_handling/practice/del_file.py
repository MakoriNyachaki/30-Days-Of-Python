from __future__ import print_function
import os

try:
    os.remove('remove.txt')
except FileNotFoundError as e:
    print(e)
