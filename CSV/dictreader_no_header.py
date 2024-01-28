# dictreader_no_header.py

# The DictReader constructor takes an iterable (i.e. a file object) 
# and an optional list of field names. 
# If omitted, the DictReader will assume the first row contains the field definition.
import csv

with open('chart_no_header.csv', newline='') as file:
    # This CSV has no header, so we must define the field names
    csv_reader = csv.DictReader(file, ['date', 'open', 'high', 'low', 'close'])
    for row in csv_reader:
        print(row)