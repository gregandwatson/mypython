#!/usr/bin/python

import os
import csv

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 10/Practice files"

with open(os.path.join(my_path, "wonka.csv"), "rb") as my_file:
	my_file_reader = csv.reader(my_file)
	next(my_file_reader) #skips over first row of file
	for first_name, last_name, reward in my_file_reader:
		print "{} {} got: {}".format(first_name, last_name, reward)
