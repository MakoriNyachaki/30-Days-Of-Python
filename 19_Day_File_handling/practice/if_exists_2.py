from __future__ import print_function
from pathlib import Path

path = Path('write.txt')

if path.is_file():
    print(f'The file {path} exists')
else:
    print(f'The file {path} does not exixst')
