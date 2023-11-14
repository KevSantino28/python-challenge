import os
import csv
#creating pathway to read data
election_csv = os.path.join("PyPoll","Resources","election_data.csv")

#Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    #storing header
    csv_header = next(csv_file)
    
    #Setting variables
    total_votes = 0
    c_votes = 0
    d_votes = 0
    r_votes = 0

    #Calculating votes per Candidate
    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] == "Charles Casper Stockham":
            c_votes = c_votes + 1
        if row[2] == "Diana DeGette":
            d_votes = d_votes + 1
        if row[2] == "Raymon Anthony Doane":
            r_votes = r_votes + 1
    #Calculating percentage of total votes recieved & rounding the percentage to 3 decimal spots
    c_percentage = (c_votes / total_votes) * 100
    c_percentage = round(c_percentage, 3)
    d_percentage = (d_votes / total_votes) * 100
    d_percentage = round(d_percentage, 3)
    r_percentage = (r_votes / total_votes) * 100
    r_percentage = round(r_percentage, 3)


    #Printing Results
    print("Election Results")
    print("--------------------------------")
    print(f'Total Votes: {total_votes}')
    print("--------------------------------")
    print(f'Charles Casper Stockham: {c_percentage}% ({c_votes})')
    print(f'Diana DeGette: {d_percentage}% ({d_votes})')
    print(f'Raymon Anthony Doane: {r_percentage}% ({r_votes})')
    print("--------------------------------")
    #Determining who won with if else statements
    if c_votes > d_votes and c_votes > r_votes:
        print(f'Winner : Charles Casper Stockham')
    elif d_votes > c_votes and d_votes > r_votes:
        print(f'Winner: Diana DeGette')
    else:
        print(f'Winner: Raymond Anthony Doane')
    print("-------------------")



#Creating outPut file
output_file = os.path.join("Election_Data_Final.csv")

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    #Writing Results
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------------"])
    writer.writerow(["Total Votes: 369711"])
    writer.writerow(["---------------------------"])
    writer.writerow(["Charles Casper Stockham: 23.049% (85213)"])
    writer.writerow(["Diana DeGette: 73.812% (272892)"])
    writer.writerow(["Raymon Anthony Doane: 3.139% (11606)"])
    writer.writerow(["---------------------------"])
    writer.writerow(["Winner: Diana DeGette"])
    writer.writerow(["---------------------------"])

   
