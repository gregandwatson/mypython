#!/usr/bin/python

name = raw_input("Enter in file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
time_list = list()
dictlist = dict()
for lines in handle:
	if lines.startswith('From '):
		words = lines.split()
		time = words[5]
		hour = time.split(':')
		time_list.append(hour[0])

for hour in time_list:
	dictlist[hour] = dictlist.get(hour,0) + 1
for k,v in sorted(dictlist.items()):
	print k,v
print dictlist
