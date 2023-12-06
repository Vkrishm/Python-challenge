# Import dependencies
import csv
import os

# Files to load and output
csv_path = os.path.join('D:/Data Boot Camp/Module 3 challenge/Python-challenge/PyPoll/Resources/election_data.csv')
file_to_output = os.path.join('D:/Data Boot Camp/Module 3 challenge/Python-challenge/PyPoll/Analysis/election_results.txt')

# Track various parameters
no_of_votes = []

# Read in the CSV file
with open(csv_path) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row
    csv_header = next(csv_reader)

    # Gathering total votes
    for row in csv_reader:
        if row[2] == "Candidate":
            continue
        no_of_votes.append(row[2])

# Print and write results to a text file
with open(file_to_output, "w") as txtfile:
    print("Election Results")          # Printing text to terminal
    print('-------------------------') 
    print('Total Votes: ' + str(len(no_of_votes))) 
    print('-------------------------') 
    txtfile.write("Election Results\n") # Writing to text file
    txtfile.write('-------------------------\n')
    txtfile.write('Total Votes: ' + str(len(no_of_votes)) + '\n')
    txtfile.write('-------------------------\n')
    
    candidates = set(no_of_votes)
    highest = 0
    winner = ""
   
    for candi in list(candidates):
        if no_of_votes.count(candi) > highest:
            highest = no_of_votes.count(candi)
            winner = candi
        print(f'{candi}: ({"{:.3f}".format(no_of_votes.count(candi) / len(no_of_votes) * 100)}%) {no_of_votes.count(candi)}')
        txtfile.write(f'{candi}: ({"{:.3f}".format(no_of_votes.count(candi) / len(no_of_votes) * 100)}%) {no_of_votes.count(candi)}\n')
    print('-------------------------')
    print('Winner: ' + winner)
    print('-------------------------')
    txtfile.write('-------------------------\n')
    txtfile.write('Winner: ' + winner + '\n')
    txtfile.write('-------------------------\n')