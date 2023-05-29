from __future__ import print_function

"""
Declare a function named capitalize_list_items. It takes a list as a
parameter and it returns a capitalized list of items
"""
def capitalize_list_items(ls):
    for item in ls:
      item = item.capitalize()
    lst = [item]
    return lst

food_staff = ['potato', 'tomato', 'mango', 'milk'];

print(capitalize_list_items(food_staff))
