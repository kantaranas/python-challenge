#define libraries
import os
import csv

#file to analyze
budget_csv_path = os.path.join("./Resources/budget_data.csv")

#define varibles to calculate
#Total number of months in dataset
months = []

#Net total of Profit/Losses
profit = []

#open and read the csv file to calculate number of date rows as well as to sum total profits
with open(budget_csv_path, "r", newline="") as revenuedata:
    csvreader = csv.reader(revenuedata, delimiter=',')
    next(csvreader)
    #count the rows in the csv file
    row_count = 0
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])
        row_count += 1
        #print(row_count)


#Loop through all the rows in column 1 to get the average profit/losses 
#new formula to calculate average revenue change
revenue_change = []
for x in range(1, len(profit)):
    revenue_change.append((int(profit[x]) - int(profit[x-1])))
    
#subtract the last month profit from the first month
revenue_average = round(sum(revenue_change) / len(revenue_change))
#print(revenue_average)


# Display summary header
print("\nFinancial Analysis", "\n-------------------------------------------")

# Display the total number of months
print("Total Months:", row_count)


# Display the total revenue of the csv file
revenue_sum = 0
for i in profit:
    revenue_sum += int(i)
print("Total: $" + str(revenue_sum))


# Display the Average Revenue Change
print("Average Change: $" + str(revenue_average))

#Find the greatest increase in profit
greatest_increase = max(revenue_change)
print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "(" + "$" + str(greatest_increase) + ")")


#Find the greatest decrease in profit
greatest_decrease = min(revenue_change)
print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "(" + "$" + str(greatest_decrease) + ")")


#Export a text file with the results
file = open("./Resources/mypybank.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------------------------------------------------" + "\n")
file.write("Total Months:" + str(row_count) + "\n")
file.write("Total: $" + str(revenue_sum) + "\n") 
file.write("Average Change: $" + str(revenue_average) + "\n") 
file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "(" + "$" + str(greatest_increase) + ")" + "\n") 
file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "(" + "$" + str(greatest_decrease) + ")" + "\n")

file.close()  