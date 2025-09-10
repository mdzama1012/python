"""Python program to demonstrate, how to read a csv file."""

import csv
from typing import List, Dict


# Example-1: Reading a csv file using csv.reader(file_name).
with open("items.csv", "r") as csv_file:
    csv_iterator = csv.reader(csv_file)
    next(csv_iterator)
    for row in csv_iterator:
        print(row[0], row[1], row[2])

print("")

# Example-2: Reading a csv file using csv.DictReader(file_name).
with open("items.csv", "r") as csv_file:
    csv_iterator = csv.DictReader(csv_file)
    for dict_row in csv_iterator:
        print(dict_row["Name"], dict_row["Price"], dict_row["Count"])
