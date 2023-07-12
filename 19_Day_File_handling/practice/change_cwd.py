from __future__ import print_function
import os

'''
Change current working directory
'''

os.chdir('./script')
cwd = os.getcwd()
print(cwd)
