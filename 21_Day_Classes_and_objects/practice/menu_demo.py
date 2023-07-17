# This program tests the Menu class.

from __future__ import print_function
from class_menu import Menu

mainMenu = Menu()
mainMenu.addOption("Create an account")
mainMenu.addOption("Log in to an exixting account")
mainMenu.addOption("Help")
mainMenu.addOption("Quit")
choice = mainMenu.getInput()

print(f'Input: {choice}\n')
