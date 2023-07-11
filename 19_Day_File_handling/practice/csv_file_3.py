from __future__ import print_function
import csv

'''
Reading a csv file using DictReader
'''

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    next(csv_reader)

    for line in csv_reader:
        print(f"The area of {line['name']} is {line['area']} km2")
