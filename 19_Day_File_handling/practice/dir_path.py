from __future__ import print_function
import os

'''
Join and split a path to directory
'''
# path join

fp = os.path.join('temp', 'python', 'lists')
print(f'\n{fp}')

# path split

fs = os.path.split(fp)
print(f'\n{fs}')
