#!/usr/bin/python
fname = raw_input('Enter a file name: ')

try:
	fh = open(fname, 'r')
except:
	print "The file", fname, "cannot be opened. No such file exists"
	exit()
for line in fh:
	line = line.rstrip()
#inp = fh.read()
	print line
