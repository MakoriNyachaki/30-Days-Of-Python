from __future__ import print_function
import csv

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line) # Header
            print('Data:')
        else:
            print(line) # Data
