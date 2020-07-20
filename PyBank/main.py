import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#Look at the data
with open(csvpath) as f:
    reader = csv.reader(f, delimiter=':')
    fieldnames = ["Date", "Profit/Losses"]
    for row in reader:
        print (row)
   
#The net total amount of "Profit/Losses" over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    num_rows = 0
    for row in open(csvpath):
        num_rows += 1

    print(num_rows)

# The greatest decrease in losses (date and amount) over the entire period
with open(csvpath) as csvfile:
    Date_array =[]
    Value_array = list()
    next(csvfile)
    for line in csvfile:
            array = line.split(',')
            first_item = array[0]
            second_item = array[1].rstrip("\n")
            Date_array.append(first_item )
            Value_array.append (int(second_item))
            
    total_profit = sum(Value_array)
    loser = min(Value_array)
    winner = max(Value_array)

    Avg_Budget = (sum(Value_array)/len(Value_array))
  
   # printing the first element 
    print(Value_array)

    print("The average of the changes in Profit/Losses over the entire period", Avg_Budget)
    print("total of the profit and loss:", total_profit)
    print("Smallest element is:", loser)
    print("Biggest element is:", winner)
