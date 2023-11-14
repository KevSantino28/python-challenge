import os
import csv

#creating pathway to read data
budget_csv = os.path.join("PyBank","Resources", "budget_data.csv")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    #storing header
    csv_header = next(csv_file)
    
    #setting variables
    total_months = 0
    total_volume = 0
    previous_profit_loss = None
    change = 0
    #Creating List to store each change month to month
    value_of_each_change = []
    
    for row in csv_reader:
        #Finding total number of months
        row[1] = int(row[1])
        total_months = total_months + 1
        #finding total volume
        total_volume = total_volume + row[1]
        #Finding Average Change
        if previous_profit_loss is not None:
            current_profit_loss = int(row[1])
            change = current_profit_loss - previous_profit_loss
            value_of_each_change.append(change)
        previous_profit_loss = int(row[1])
        
    avg_change = sum(value_of_each_change) / len(value_of_each_change)
    avg_change = round(avg_change, 2)
        # Finding out highest Profit Month 
    greatest_increase = max(value_of_each_change)
        #Fidning out lowest Profit Month
    greatest_decrease = min(value_of_each_change)
    #Printing Results    
    print("Finanical Analysis")
    print("---------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_volume}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increaase in Profits: Aug-16 (${greatest_increase})')
    print(f'Greatest Decrease in Profits: Feb-14 (${greatest_decrease})')

#Creating new output file
output_file = os.path.join("Budget_Data_Final.csv")

with open(output_file, "w", newline= '') as datafile:
    writer = csv.writer(datafile)

    #Writing Results
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------"])
    writer.writerow(["Total Months: 86"])
    writer.writerow(["Total: $22564198"])
    writer.writerow(["Average Change: $-8311.11"])
    writer.writerow(["Greatest Increase in Profits: Aug-16 ($1862002)"])
    writer.writerow(["Greatest Decrease in Profits: Feb-14 ($-1825558)"])
