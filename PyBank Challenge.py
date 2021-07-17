#!/usr/bin/env python
# coding: utf-8

# In[2]:


# PyBank Challenge

# Dependencies
import os
import csv

ProfitList = []
DateList = []
TotalMonths = 0

# Identify files
BudgetDataFile = os.path.join("budget_data.csv")
AnalysisFile = os.path.join("budget_analysis.txt")

# Open and read the file
with open(BudgetDataFile) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")

    # Identify the header
    csv_header = next(csv_reader)
    print(csv_header)
    
    
    # Loop throught the rows
    for row in csv_reader:        
        
        # Count the total months
        TotalMonths = TotalMonths + 1
        
        # Create a list out of the columns
        ProfitList.append(int(row[1]))
        DateList.append(row[0])
        
    # Check the total months
    print(TotalMonths)
    
    # Check the net profits and losses
    print(sum(ProfitList))


# In[28]:


# Determine the list length
length = len(ProfitList)
# print(length)

# Define a new list for each change in profit
ProfitChangeList = []
NewDateList = []

# Create a new list for each change in profit and a new list for the associated dates
for i in range(1,length):
    change = ProfitList[i] - ProfitList[i-1]
    ProfitChangeList.append(change)
    
    vdate = DateList[i]
    NewDateList.append(vdate)

# Calculate the average change in profit
AverageChange = round((sum(ProfitChangeList)/length),)
print(AverageChange)

# Find the greatest increase in price change
GreatestIncrease = max(ProfitChangeList)
print(ProfitChangeList.index(GreatestIncrease))
print(f'{NewDateList[24]} (${GreatestIncrease})')

# Find the greatest decrease in price change
GreatestDecrease = min(ProfitChangeList)
print(ProfitChangeList.index(GreatestDecrease))
print(f'{NewDateList[43]} (${GreatestDecrease})')


with open (AnalysisFile,'w',newline='') as txtfile:
    writer = csv.writer(txtfile, delimiter=",")
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------------"])
    writer.writerow([f'Total Months: {TotalMonths}'])
    writer.writerow([f'Average Change: ${AverageChange}'])
    writer.writerow([f'Greatest Increase in Profits: {NewDateList[24]} (${GreatestIncrease})'])
    writer.writerow([f'Greatest Decrease in Profits: {NewDateList[43]} (${GreatestDecrease})'])
    

    
# List comprehension practice
# ProfitChangeList = [ProfitList[i] - ProfitList[i-1] for i in range(1,length)]
# print(test)


# In[ ]:




