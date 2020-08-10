# bounce.py
#
# Exercise 1.5

currentHeight = 100

# e is basically the co-efficient of restitution. At times, I miss Physics.
e = (3/5) 

for i in range (0, 10):
	currentHeight = round(currentHeight*e,4)
	print("Height after bounce "+str(i+1)+" is "+str(currentHeight))