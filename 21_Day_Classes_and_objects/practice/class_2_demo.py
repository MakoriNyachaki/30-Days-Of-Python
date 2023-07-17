from __future__ import print_function
from class_2 import Counter

"""
Demonstrates the working of the counter class(class_2)
"""

tally = Counter()
#tally.reset()
tally.click()
tally.click()

print(f'Value: {tally.getValue()}\n')

tally.click()
tally.click()

print(f'Value: {tally.getValue()}\n')
