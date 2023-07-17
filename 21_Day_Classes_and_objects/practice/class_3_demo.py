from __future__ import print_function
from class_3 import Counter

"""
Counter class using the string value instead of integer
"""


tally = Counter()
tally.reset()
tally.click()
tally.click()

print(f'Value: {tally.getValue()}\n')
