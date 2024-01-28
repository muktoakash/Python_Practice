# namedtuple_csv.py

# Namedtuples are useful to store this type of information.
# Having this data structure allows us to accurately and explicitly describe its content. 

import csv
from collections import namedtuple

Performance = namedtuple('Performance', ['date', 'open', 'high', 'low', 'close'])

with open('chart_no_header.csv', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        performance = Performance(*row)
        print(performance)

    #Why does this not like going through the second for loop?
    #The syntax is fine, since commenting out the first loop, program runs for 2nd loop
    #But having the first loop means second loop is not accessed?
    for row in csv_reader:
        performance = Performance(*row)
        report = f'Closed at ${performance.close} on {performance.date}'
        print(report)