#!/usr/bin/python

try:
	number = int(raw_input("Enter an integer: "))
except ValueError:
	print "That was not an integer."
