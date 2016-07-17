#!/usr/bin/python

import re

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:', line):
		print line
	if line.startswith('From:'):
		print line
