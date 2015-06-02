#!/usr/bin/python

new_file = raw_input('Type in the name of the file you wish to open: ')
fh=open(new_file)
lst = list()
for line in fh:
	words = line.split()
	for each_word in words:
		if each_word in lst: continue
		lst.append(each_word)
lst.sort()
print lst

