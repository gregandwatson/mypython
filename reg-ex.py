#!/usr/bin/python
import re

hand = open('mbox-short.txt')
for line in hand:
	if re.search('^X-\S+:', line):
#	if line.startswith('From:'):
		print line
#fh = hand.read()
#print fh.find('From:')
