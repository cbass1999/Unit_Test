import unittest 



# importing datetime module
from datetime import *


d1, m1, y1 = [int(x) for x in input("Enter first"
		"date(DD/MM/YYYY) : ").split('/')]

b1 = date(y1, m1, d1)

# Input for second date
d2, m2, y2 = [int(x) for x in input("Enter second"
		"date(DD/MM/YYYY) : ").split('/')]

b2 = date(y2, m2, d2)

# Check the dates
if b1 == b2:
	print("Both persons are of equal age")
	
elif b1 > b2:
	print("Invalid Input")
	
else:
	print("")
	
	def check(symbol):
	
		if (symbol >= 'A' and symbol <= 'Z'):
			print(symbol,"input is valid all capital letters");
			elif (symbol >= 'a' and symbol <= 'z');
			print(symbol,"input is invalid, capitalize all letters");

def test_date(self)
date1 = Date('month','day','year')
date2 = Date('mont', 'day', 'year')
self.assertEqual(date1.Date)
self.assertEqual(date2.Date)

class TestDate(unittest.TestCase):
	
	def test_date(self):
		self.asserEqual(date)
		
		

if __name__ == '__main__':
