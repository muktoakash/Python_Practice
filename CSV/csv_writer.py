# The CSV writer operates on open files

# Rows can also be written in bulk using the .writerows() method.

import csv 

with open('writer.csv', 'w', newline='') as file:
    writer = csv.writer(file)  # Create the writer
    writer.writerow(['City', 'Province'])  # First row
    writer.writerow(['Toronto', 'ON'])
    writer.writerow(['Montreal', 'QC'])

# The DictWriter provides the ability to write dictionaries to CSV files.
# we have to explicitly tell the writer to include headers using the writeheader() method:

cities = [
    {'city': 'Toronto', 'province': 'ON'},
    {'city': 'Montreal', 'province': 'QC'}
]

with open('cities.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, ['city', 'province'])
    writer.writeheader()  # Write the header
    writer.writerows(cities)  # Write all the rows at once