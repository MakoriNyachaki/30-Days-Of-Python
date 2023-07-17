from __future__ import print_function

"""
Counter class to count people who have attended a concert
"""


class Counter:
    _value = 0

    def click(self):
        """
        Advances the _value by 1
        """
        self._value += 1

    def getValue(self):
        """
        Returns how many times the counter has been clicked
        """
        return self._value

    def reset(self):
        """
        Sets the value of _value to zero
        """
        self._value = 0
