#!/usr/bin/python

import re

fh = open('mbox-short.txt', 'r')
for line in fh:
	y = re.findall('[0-9]+', line)
	print y
#	for biggest_number in y:
#		if biggest_number < 1000:
#			print biggest_number
#		else:
#			print 'Number is smaller than 10000'
