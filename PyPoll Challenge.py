#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PyPoll Challenge

# Dependencies
import os
import csv

TotalVotes = 0
CandidateVotes = []
Candidates = []

# Identify files
VoterDataFile = os.path.join("election_data.csv")
AnalysisFile = os.path.join("election_analysis.txt")

# Create a function to analyze the poll data
def PollOutcome(PollData):
    
    # Assign variables to columns for clarity
    voter = int(PollData[0])
    county = str(PollData[1])
    candidate = str(PollData[2])
    
    # Create variables for desired calculations
    
    

# Open and read the file
with open(VoterDataFile) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    
    # Identify the header
    csv_header = next(csv_reader)
    print(csv_header)
    
    # Loop through the rows
    for row in csv_reader:
        
        # Count the votes
        TotalVotes = TotalVotes + 1
        
        # Make a list of all votes
        CandidateVotes.append(row[2]) 
        
    print(TotalVotes)        
    


# In[36]:


# Loop through the votes
for Candidate in CandidateVotes: 
        
        # Determine if the candidate is already in list of candidates
        # If not, add it to the list of candidates
        if Candidate not in Candidates:
            Candidates.append(Candidate)

print(Candidates)

# Count the number of votes for each candidate
KhanVotes = CandidateVotes.count("Khan")
CorreyVotes = CandidateVotes.count("Correy")
LiVotes = CandidateVotes.count("Li")
OTooleyVotes = CandidateVotes.count("O'Tooley")

# Make sure the sum of the counts matches the total votes
# TotalVotesCheck = KhanVotes + CorreyVotes + LiVotes + OTooleyVotes
# TotalVotesCheck

# Find the percentage of votes for each candidate
PercentKhan = (KhanVotes/TotalVotes)*100
PercentCorrey = (CorreyVotes/TotalVotes)*100
PercentLi = (LiVotes/TotalVotes)*100
PercentOTooley = (OTooleyVotes/TotalVotes)*100

# Make sure the sum of the percentages is equal to 100
# TotalPercent = PercentKhan+PercentCorrey+PercentLi+PercentOTooley
# TotalPercent


# In[37]:


# Find the winner based on popular vote
PollBreakdown = {"Khan":KhanVotes,"Correy":CorreyVotes,
                 "Li":LiVotes,"O'Tooley":OTooleyVotes}
PollBreakdown

# Define what makes a winner
WinningCandidate = max(PollBreakdown.values())

# Loop through the dictionary of candidates and their vote counts
# And return the name of the candidate that matches the winning votes
for name, votes in PollBreakdown.items():
    if votes == WinningCandidate:
        Winner = name
Winner


# In[46]:


# Create a txt file for the analysis results
with open (AnalysisFile,'w',newline='') as txtfile:
    writer = csv.writer(txtfile,delimiter=",")
    
    writer.writerow(["Election Results"])
    writer.writerow(["--------------------------------------"])
    writer.writerow([f'Total Votes: {TotalVotes}'])
    writer.writerow(["--------------------------------------"])
    writer.writerow([f'Khan: {int(PercentKhan)}% ({KhanVotes})'])
    writer.writerow([f'Correy: {int(PercentCorrey)}% ({CorreyVotes})'])
    writer.writerow([f'Li: {int(PercentLi)}% ({LiVotes})'])
    writer.writerow([f"O'Tooley: {int(PercentOTooley)}% ({OTooleyVotes})"])
    writer.writerow(["--------------------------------------"])
    writer.writerow([f'Winner: {Winner}'])
    writer.writerow(["--------------------------------------"])    

