#!/usr/bin/python

fname = raw_input("Enter file name: ")
fh = open(fname)
lines = fh.read()
lines = lines.upper()

print lines
