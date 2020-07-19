import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")

found = False

with open(csvpath) as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print row

#The net total amount of "Profit/Losses" over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    num_rows = 0
    for row in open(cvspath):
        num_rows += 1

    print(num_rows)

#with open("csvpath")) as fin:
 # headerline = fin.next()
  #total = 0
  #for row in csv.reader(fin):
   # print col # for troubleshooting
    #for col in row[1]:
     # total += int(col)
  #print total

#for row in csvpath:
 #       header = next(csvpath)
  #      if row[0] == Emmp ID:
   #         print("For" + row[0] + "  " + row[1])

    #        found = True


    #if found is False:
     #   print("Sorry about this, we don't seem to have what you are looking for!")


avg_mass = sum(csvpath) / len(csvpath)
print "avg of mass: ", avg_mass

#The greatest increase in profits (date and amount) over the entire period
with open('american_colleges__universities_1993.csv', 'rU') as f:
    reader = csv.reader(f)
    answer = 0
    for column in reader :
        answer = 0
        for i in column[14]:
            if i>answer:
                answer = i
print answer



