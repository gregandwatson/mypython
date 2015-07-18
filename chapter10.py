#!/usr/bin/python

#fh = open("hello.txt", "a")
#lines_to_write = ["\nI bomb atomically, socrates philosophies\n"]
#fh.writelines(lines_to_write)
fh = open("hello.txt", "r")
for line in fh.readlines():
	print line,
fh.close()
