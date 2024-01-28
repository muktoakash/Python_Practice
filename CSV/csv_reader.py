# csv_reader.py

# The CSV reader returns an iterable
#  which returns a list of field values.
#  By default, these will always be strings.

import csv  # The CSV module

with open('chart.csv', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(*row, sep='\t')   # Unpack the fields, and separate with tabs