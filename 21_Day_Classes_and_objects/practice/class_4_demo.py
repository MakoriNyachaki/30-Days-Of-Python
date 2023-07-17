from __future__ import print_function
from class_4 import CashRegister

register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)

print(f'Total number of items: {register1.getCount()} ' +
      f'Total cost: {register1.getTotal()} ' +
      f'Change: {register1.giveChange(5)}\n')

register2 = CashRegister()
register2.addItem(1.90)

print(f'Total number of items: {register2.getCount()} ' +
      f'Total Cost: {register2.getDollars()} '
      f'Change: {register2.giveChange(5)}\n')
