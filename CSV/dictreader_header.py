# dictreader_header.py

# For the CSV with headers,
#  we can omit the field names definition and let the reader use the first row:

import csv

with open('chart.csv', newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
         print('Opened at $', row['open'], ' on ', row['date'], sep='')