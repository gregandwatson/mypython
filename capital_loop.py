#!/usr/bin/python

from capitals import capitals_dict
import random
answer = ''
state = random.choice(capitals_dict.keys())
#print state
capital_city = capitals_dict[state]
#print capital_city
count = 0
while count == 0:
	answer = raw_input('What is the capital of ' + state + '? ')
	if answer == capital_city or answer == capital_city.lower():
		print "Correct"
		count = count + 1
	elif answer == "exit" or answer == "Exit":
		print "Goodbye"
		break

