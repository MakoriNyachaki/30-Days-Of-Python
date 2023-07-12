from __future__ import print_function
import os

dir = os.path.join("C:\\", "temp")
print(dir)

if os.path.exists(dir) or os.path.isdir(dir):
    print(f'The {dir} is a directory')
