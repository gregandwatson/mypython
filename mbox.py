#!/usr/bin/python

fname = raw_input("Enter the name of the file you wish to open: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	print line
	ftext = line.find("0")
	print ftext
	num_text = float(line[20:])
	print num_text
	total = total + num_text
	count = count + 1
	print count
	print total
final = total / count
print final
print "Done"
