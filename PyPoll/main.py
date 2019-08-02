# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

import os 
import csv

file_num = 2

file = os.path.join('..','..','Instructions','PyPoll','Resources','election_data.csv')

# create dictionary to be used for candidate name and vote count
poll = {}

# set variable, total votes, to zero for count
total_votes = 0

#read csv and parse data into lists
with open(file,'r') as csvfile:
    csvread = csv.reader(csvfile)

    # skip header line
    next(csvread, None)

    # create dictionary from file useing column 3 as keys, using each name only once
    # count votes for each candidate as entris
    # keep total vote count by counting up from 1 for eahc loop (#of rows w/o header)
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] +1
        else:
            poll[row[2]] = 1

# create empty list for candidates and his/her vote count
candidates = []
num_votes = []

# take dictionary keys and values, add them to lists
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# create vote percent list:
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

# create winner list for winners
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# make winner list a string with first entry
winner = winner_list[0]

# onyl run if there is a tie and puts additional winners into a string separated by comma
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + "," + winner_list[w]

# prints to file
output_file = os.path.join('..','PyPoll','election_summary.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())

