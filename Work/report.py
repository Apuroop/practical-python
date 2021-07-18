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

current_portfolio = read_portfolio("Data/portfolio.csv")

total_portfolio_value = 0

for stocks in current_portfolio:
	total_portfolio_value += stocks["Stock Count"]*stocks["Stock Price"]


print ("Total value of Current Portfolio: ", total_portfolio_value)