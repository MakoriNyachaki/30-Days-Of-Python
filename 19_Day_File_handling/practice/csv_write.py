from __future__ import print_function
import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('countries.csv', 'w', encoding="utf8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerow(data)
