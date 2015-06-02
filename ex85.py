#!/usr/bin/python

file = raw_input('Enter file name: ')
fh = open(file)
count = 0
for line in fh:
	if not line.startswith('From ') : continue
	each_line = line.split()
	print each_line[1]
	count = count + 1
print "There were", count, "lines in the file with From as the first word"
