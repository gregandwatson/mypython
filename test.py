#!/usr/bin/python

import os

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 10/Practice files"

my_file = os.path.join(my_path,"output.txt")

fh = open(my_file, "r")
for new_line in fh:
	print new_line
