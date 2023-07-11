from __future__ import print_function
import csv
'''
Reading country.csv and calculating the total area
'''
total_area = 0

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)

    for line in csv_reader:
        total_area += float(line[1])

print(total_area)
