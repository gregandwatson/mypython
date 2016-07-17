#!/usr/bin/python

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line
    line = line.rstrip()
    line_number = float(line[19:])
    count = count + 1
    sum = sum + line_number 
average = sum / count
print average
print "Done"
