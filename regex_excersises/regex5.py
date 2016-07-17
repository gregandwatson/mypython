#!/usr/bin/python

import re

file = open('mbox-short.txt', 'r')
for line in file:
	message = re.findall('^Message-ID: <\S+@\S+', line)
	print message
