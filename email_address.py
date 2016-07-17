#!/usr/bin/python

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for lines in fh:
	if lines.startswith('From:'):
		lines=lines.split()
		print lines[1]
		count = count + 1
print "There were", count, "lines in the file with From as the first word"
