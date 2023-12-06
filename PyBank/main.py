# Import dependencies
import csv
import os

# Files to load and output
csv_path = os.path.join('D:/Data Boot Camp/Module 3 challenge/Python-challenge/PyBank/Resources/budget_data.csv')
file_to_output = os.path.join('D:/Data Boot Camp/Module 3 challenge/Python-challenge/PyBank/Analysis/budget_analysis.txt')

# Track various parameters
count_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
net_profit_loss = 0

# Read in the CSV file
with open(csv_path) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row
    csv_header = next(csv_reader)
    
    # Extract first row to avoid appending to net_change_list
    first_row_data = next(csv_reader)
    count_months += 1
    net_profit_loss += int(first_row_data[1])
    prev_net = int(first_row_data[1])
    for row in csv_reader:
        # Track the total
        count_months += 1
        net_profit_loss += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)
# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count_months}\n"
    f"Total: ${net_profit_loss}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# Print the output (to terminal)
print(output)
# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)