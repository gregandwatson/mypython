#!/usr/bin/python

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
#	if re.search('^From:', line) :
	if re.search('\s<.*org', line):
		y = re.findall('\s<.*org', line)
		print y
