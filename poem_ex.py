#!/usr/bin/python

with open("poem.txt", "r") as fh:
	for lines in fh.readlines():
		print lines

