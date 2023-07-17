from __future__ import print_function

"""
A change in the implementation of the Counter class
We will use the string of characters instead of an integer
"""


class Counter:

    def reset(self):
        self.strokes = ""

    def click(self):
        self.strokes += "|"

    def getValue(self):
        return self.strokes
