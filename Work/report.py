# report.py
#
# Exercise 2.4
# For this attempt, I will be making a report that stores a portfolio in dicts & displays the total portfolio

import csv
from pprint import pprint

def read_portfolio(FilePath):
	portfolio = []
	with open (FilePath, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			current_values = {"Stock Name": row[0], "Stock Count": int(row[1]), "Stock Price": float(row[2])}
			portfolio.append(current_values)
	return (portfolio)

def read_current_prices(FilePath):
	with open(FilePath, "rt") as f:
		rows = csv.reader(f)
		price_dict = {}
		for row in rows:
			# added this because the file might contain some empty lines which cause this to break. 
			# the better approach might be to try-catch this instead. 
			# will do that as the next example
			if (len(row) == 0): 
				continue
			else:
				price_dict[row[0]] = float(row[1])
	return (price_dict)

current_portfolio = read_portfolio("Data/portfolio.csv")

current_stock_prices = read_current_prices("Data/prices.csv")

# pprint(current_stock_prices)

starting_portfolio_value = 0
current_portfolio_value = 0

for stocks in current_portfolio:
	# print(stocks)
	starting_portfolio_value += stocks["Stock Count"]*stocks["Stock Price"]
	current_portfolio_value += current_stock_prices[stocks["Stock Name"]]*stocks["Stock Count"]

portfolio_status = current_portfolio_value-starting_portfolio_value

if (portfolio_status <=0):
	print("Your current loss is: ", portfolio_status)
	print("You cannot retire! :( ")
else:
	print("Your current gain is: ", portfolio_status)
	print("You could possibly retire! :D")