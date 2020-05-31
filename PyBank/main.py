# import modules: os , csv
import os
import csv

#define the path to access the csv file with raw data
csvpath = os.path.join("Resources-PyBank", "budget_data.csv")

#create empty lists: list of months , monthly profits , and profit changes
month_count = []
first_monthly_profit = []
next_month = []
next_monthly_profit = []
profit_change = []

#create net profit total, greatest increase, and greatest decrease that all start at zero
net_profit_total = 0
greatest_increase = 0
greatest_decrease = 0

#open and read data in csv file
with open(csvpath,'r') as budget_data:
    read_data = csv.reader(budget_data, delimiter = ',')
    #read header
    data_header = next(read_data)
    #read rows and collect data
    for row in read_data:
        month_count.append(row[0])
        net_profit_total = net_profit_total + int(row[1])
        first_monthly_profit.append(int(row[1]))
        next_month.append(row[0])
        next_monthly_profit.append(int(row[1]))
    
    first_monthly_profit.pop(len(month_count)-1)
    next_month.pop(0)
    next_monthly_profit.pop(0)

#zip monthly profit lists and calculate profit changes
changes = zip(first_monthly_profit,next_monthly_profit)
for change in changes:
    profit_change.append(change[1] - change[0])

#calculate the average change in profit
average_change = (round(sum(profit_change) / len(profit_change),2))


#find the month with greatest increase and decrease
change_by_month = zip(next_month,profit_change)
# print(next_month)
# print(profit_change)
# output_file = os.path.join("change_by_month.csv")
# with open(output_file,"w") as datafile:
#     writer = csv.writer(datafile)
#     writer.writerows(change_by_month)


for each_change in change_by_month:
    if int(each_change[1]) > greatest_increase:
        greatest_increase = int(each_change[1])
        greatest_increase_month = each_change[0]
    elif int(each_change[1]) < greatest_decrease:
        greatest_decrease = int(each_change[1])
        greatest_decrease_month = each_change[0]



print("""
Financial Analysis
----------------------------
""")
print(f'Total Months: {len(month_count)}')
print(f'Total net Profit: ${net_profit_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
print(" ")
