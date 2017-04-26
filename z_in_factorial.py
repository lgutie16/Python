#https://www.hackerearth.com/problem/algorithm/trailing-zeros/
from math import factorial
n = input("Inter a number: ")
if(n>1 and n<1000):
	fac = factorial(n)
	factSTR = str(fac)
	number = factSTR.count("0", 0, len(factSTR))
	print number

	