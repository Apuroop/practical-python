# This is to test out dicts to store details from a csv file.
# Ex. 2.6
import csv
from pprint import pprint

def parse_prices(FilePath):
	with open(FilePath, "rt") as f:
		rows = csv.reader(f)
		header = next(rows)
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

current_stock_prices = parse_prices("Data/prices.csv")

pprint(current_stock_prices)