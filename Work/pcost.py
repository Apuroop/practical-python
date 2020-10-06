# pcost.py
#
# Exercise 1.27

data_variable = open("Data/portfolio.csv", "rt")
data_header = next(data_variable).split(",")

stock_name=[]
stock_count=[]
stock_price=[]
for line in data_variable:
	row_data = line.split(",")
	stock_name.append(row_data[0])
	stock_count.append(row_data[1])
	stock_price.append(row_data[2].strip())

total_price = 0
for i in range (0, len(stock_count)):
	total_price += (int(stock_count[i])*float(stock_price[i]))

print(total_price)