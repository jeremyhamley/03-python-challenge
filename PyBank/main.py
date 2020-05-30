# import modules: os , csv
import os
import csv

#define the path to access the csv file with raw data
csvpath = os.path.join("Resources-PyBank", "budget_data.csv")

#create empty lists: list of months , monthly profit totals , and profit changes
month_count = []
monthly_profit = []
profit_open = []
next_monthly_profit = []
profit_change = []

#create net profit total that starts at zero
net_profit_total = 0

#open and read data in csv file
with open(csvpath,'r') as budget_data:
    read_data = csv.reader(budget_data, delimiter = ',')

    #read header
    data_header = next(read_data)

    #read rows and collect data
    for row in read_data:
        month_count.append(row[0])
        net_profit_total = net_profit_total + int(row[1])
        monthly_profit.append(row[1])
        profit_open.append(row[1])

next_monthly_profit.append(monthly_profit[1])


for profit in monthly_profit:
    monthly_profit.pop(0)
    next_monthly_profit.append(monthly_profit[0+1])
print(next_monthly_profit)







#print(profit_open)


#for this_monthly_profit in monthly_profit:
    #next_monthly_profit.append(monthly_profit[1])



    #profit_change.append(int(monthly_profit[1])-int(monthly_profit[0]))
    #  #print(len(profit_change))





print("""
Financial Analysis
----------------------------
""")

print(f"Total Months: {len(month_count)}")
print(f"Total net Profit: ${net_profit_total}")
#print(f"Average Change in profit: ${profit_change}")

