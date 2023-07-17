from __future__ import print_function

"""
Cash register class
"""


class CashRegister:
    """
    Constructor
    """
    def __init__(self, taxRate):
        self._itemCount = 0
        self._totalPrice = 0.0
        self._taxableTotal = 0.0
        self._taxRate = taxRate

    """
    Adds an item and computes the totalprice
    """
    def addItem(self, price, taxable):
        self._itemCount += 1
        self._totalPrice += price
        if taxable:
            self._taxableTotal += price

    """
    return the total price of the items
    """
    def getTotal(self):
        return self._totalPrice + self._taxableTotal * self._taxRate / 100

    """
    returns the item count
    """
    def getCount(self):
        return self._itemCount

    """
    resets the item count and totalPrice
    """
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        self._taxableTotal = 0.0

    """
    Gets the total cost in dollars without cents
    """
    def getDollars(self):
        return round(self.getTotal())

    """
    Takes the customer payment and determines the change
    Gives the change to the customers
    """
    def giveChange(self, payment):
        return payment - self.getTotal()
        self.clear()
