#!/usr/bin/python

fh = open('mbox-short.txt')
for lines in fh:
	line = lines.rstrip()
	if line.startswith("Received:"):
		print line[18:]
