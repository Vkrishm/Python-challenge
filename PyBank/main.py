import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join('D:/Data Boot Camp/Module 3 challenge/Python-challenge/PyBank/Resources/budget_data.csv')

# CSV headers: Date, Profit/Losses
date = [0]
Profit_losses = [1]


# 'Resources', 'budget_data.csv'



# Read in the CSV file
with open(csv_path) as csv_file:

    #Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Read the header row first
    csv_header = next(csv_reader)

    print(csv_reader)