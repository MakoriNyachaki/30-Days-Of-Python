from __future__ import print_function

'''
Using try except to create a file
'''

try:
    with open('docs/create.txt',  'w') as f:
        f.write("Created this file")
except FileNotFoundError:
    print("The folder docs does not exist")
