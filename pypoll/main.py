import os

# import file

import csv

csvpath = "Resources/election_data.csv"

#set variables
votes = []
candidates = []
uniquecand = []
khan = 0
correy = 0
li = 0
otooley = 0
percent = {}

# Open the CSV
with open(csvpath) as f:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(f, delimiter=',')

    #print(csvreader)
    # Loop and read lines in CSV
    for row in csvreader:
        #candidates.append(row['Candidate'])
    #uniquecand = set(candidates)
    #print(uniquecand)
        votes.append(row['Voter ID'])
        #print(votes)
        if row['Candidate'] == 'Khan':
            khan = khan + 1
        elif row['Candidate'] == 'Correy':
            correy = correy + 1
        elif row['Candidate'] == 'Li':
            li = li + 1
        else:
            otooley = otooley + 1
    # print(khan, correy, li, otooley)
    # print(len(votes))
    pk =round(khan / len(votes),2)
    pc =round(correy / len(votes),2)
    pl =round(li / len(votes),2)
    po =round(otooley / len(votes),2)
    print(pk, pc, pl, po)

    percent['Khan'] = pk
    percent['Correy'] = pc
    percent['Li'] = pl
    percent["O'Tooley"] = po

    # Print results
    print('Total Votes:', len(votes))
    print('Khan:', format(pk, ".2%"), khan)
    print('Correy:', format(pc, ".2%"),correy)
    print('Li:', format(pl, ".2%"),li)
    print("O'Tooley", format(po, ".2%"),otooley)
    print("Winner:", max(percent, key=percent.get))
# Output files
output_file = os.path.join(".", "Resources", "output.txt")
with open(output_file,"w") as file:

# Write into the output.txt file
    file.write("Election Result")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(votes)}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Khan: {format(pk,'.2%')} {khan}")
    file.write("\n")
    file.write(f"Correy: {format(pc, '.2%')} {correy}")
    file.write("\n")
    file.write(f"Li: {format(pl, '.2%')} {li}")
    file.write("\n")
    file.write(f"O'Tooley: {format(po, '.2%')} {otooley}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {max(percent,key=percent.get)}")