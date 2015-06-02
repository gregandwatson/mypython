#!/usr/bin/python

enter_file = raw_input("Enter the name of the file you want to open: ")
try:
	open_file = open(enter_file)
except:
	print "The file does not exist"
	exit()
read_file = open_file.read()
print read_file.upper()
print read_file.split()
