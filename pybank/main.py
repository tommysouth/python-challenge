import os

# import file

import csv

csvpath = "Resources/budget_data.csv"

#set variables
month = []
profitloss = []
totalpl = []
diffval = 0
difflist = []

# Open the CSV
with open(csvpath) as f:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(f, delimiter=',')

    #print(csvreader)
    # Loop and read lines in CSV
    for row in csvreader:
        # print(row)
        # Create list for dates
        month.append(row['Date'])
        # Create list for profit and losses
        profitloss.append(row['Profit/Losses'])
    # print(profitloss)
    # print(profitloss[1])
    # print(len(profitloss))
        # Change list of profit and losses to integer
        totalpf = (map(int, profitloss))
        # Calculating the difference in value between two consecutive months
    for i in range(len(profitloss)-1):
        diffval = int(profitloss[i + 1]) - int(profitloss[i])
        difflist.append(diffval)
    # print(difflist)

    maxdiff = max(difflist)
    mindiff = min(difflist)
    maxmonth = difflist.index(max(difflist))+ 1
    minmonth = difflist.index(min(difflist))+ 1
# phrint(maxdiff,mindiff)
# print(maxmonth,minmont)

# Print results
print("Financial Analysis")
print('Total Months:', len(month))
print('Total: $', sum(totalpf))
print(f"Average Change: {round(sum(difflist)/len(difflist),2)}")
print(f"Greatest Increase in Profits: {month[maxmonth]}(${(str(maxdiff))})")
print(f"Greatest Decrease in Profits: {month[minmonth]}(${(str(mindiff))})")

# Output files
output_file = os.path.join(".", "Resources", "output.txt")
with open(output_file,"w") as file:

# Write into the output.txt file
   file.write("Financial Analysis")
   file.write("\n")
   file.write("----------------------------")
   file.write("\n")
   file.write(f"Total Months: {len(month)}")
   file.write("\n")
   file.write(f"Total: ${sum(totalpf)}")
   file.write("\n")
   file.write(f"Average Change: {round(sum(difflist)/len(difflist),2)}")
   file.write("\n")
   file.write(f"Greatest Increase in Profits: {month[maxmonth]} (${(str(maxdiff))})")
   file.write("\n")
   file.write(f"Greatest Decrease in Profits: {month[minmonth]} (${(str(mindiff))})")