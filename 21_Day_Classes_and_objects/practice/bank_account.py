"""
Implements the BankAccount class
"""


from __future__ import print_function


class BankAccount:

    # constructor
    def __init__(self, initialBalance=0.0):
        self._balance = initialBalance

    # Deposit method allows one to deposit into his account
    # @param amount Amount to deposit
    def deposit(self, amount):
        self._balance += amount

    # Withdraw allows one to withdraw, a fixed penality of $10
    # if amount to withdraw is greater than the balance
    # @param amount Amount to withdraw
    def withdraw(self, amount):
        PENALTY = 10
        if amount > self._balance:
            self._balance = self._balance - PENALTY
        else:
            self._balance -= amount

    # Add interest Calculates the interest and adds it to the balance
    # @param rate Interest rate in percentage
    def addInterest(self, rate):
        interest = self._balance * rate/100
        self._balance += interest

    # Get balance show the bank account balance
    def getBalance(self):
        return self._balance
