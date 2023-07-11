from __future__ import print_function
import csv


with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the first row
    next(csv_reader)

    #  Show data
    for line in csv_reader:
        print(line)
