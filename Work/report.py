# report.py
#
# Exercise 2.4
# For this attempt, I will be making a report that stores a portfolio in tuples & displays the total portfolio

import csv

def read_portfolio(FilePath):
	portfolio = []
	with open (FilePath, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			current_values = (row[0], int(row[1]), float(row[2]))
			portfolio.append(current_values)
	return (portfolio)

current_portfolio = read_portfolio("Data/portfolio.csv")

total_portfolio_value = 0

for stock_name, stock_count, stock_price in current_portfolio:
	total_portfolio_value += stock_count*stock_price

print("Total Value of the portfolio :", total_portfolio_value)