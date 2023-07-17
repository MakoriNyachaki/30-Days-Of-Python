from __future__ import print_function
from bank_account import BankAccount

harrysAccount = BankAccount(1000.0)
harrysAccount.deposit(500.0)  # Balance is now $1500
harrysAccount.withdraw(2000.0)  # Balance is now $1490
harrysAccount.addInterest(1.0)  # Balance is now $1490 + 14.90
print("%.2f" % harrysAccount.getBalance())
print("Expected: 1504.90")
