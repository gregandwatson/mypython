!#/usr/bin/python

number = int(raw_input("Enter in a number: "))

def factors(number):
	for divisor in range(1, number+1):
		if number % divisor == 0:
			print divisor, "is a divisor of", number
	return number
factors(number)
