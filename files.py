#!/usr/bin/python
newfile = open('text.txt', 'r')
for lines in newfile:
	lines = lines.rstrip()
	if lines.startswith('Black'):
		print lines
