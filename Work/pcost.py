# pcost.py
#
# Exercise 1.27
import csv
import sys

def price_calculator(sourceFileName):
	"This new function takes in a file with the columns Stock Name, Stock Count & Stock Price. It returns the total value of the portfolio"
	data_variable = open(sourceFileName, "rt")
	data_rows = csv.reader(data_variable)
	data_header = next(data_rows)
	stock_name=[]
	stock_count=[]
	stock_price=[]
	for row in data_rows:
		stock_name.append(row[0])
		stock_count.append(row[1])
		stock_price.append(row[2])

	total_price = 0
	for i in range (0, len(stock_count)):
		try:
			total_price += (int(stock_count[i])*float(stock_price[i]))
		except ValueError:
			print("Missing Values for " +stock_name[i])

	return(total_price)

if (len(sys.argv) == 2):
	cost = price_calculator(sys.argv[1])
	print("Total portfolio value: "+ str(cost))
else:
	print("Incorrect values submitetd. Please enter the arguments as python <program name.py> <path to file>")
