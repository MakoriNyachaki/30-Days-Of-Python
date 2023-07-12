from __future__ import print_function
import os

try:
    os.rename('file.txt', 'renamed.txt')
except FileNotFoundError:
    print('file.txt not found')
