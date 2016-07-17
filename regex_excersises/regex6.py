#!/usr/bin/python

import re
list_of_numbers =[] 
final_total = 0
file = open('regex_sum_198997.txt')
for line in file:
	line = line.rstrip()
	numbers = re.findall('[0-9]+', line)
	for number in numbers: 
		list_of_numbers.append(number)
print numbers

for number in list_of_numbers:
	number = int(number)
	final_total = final_total + number
print final_total
