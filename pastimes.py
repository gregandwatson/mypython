#!/usr/bin/python

import csv
import os

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 10/Practice files"
with open(os.path.join(my_path, "pastimes.csv"), "rb") as my_file:
	my_file_reader = csv.reader(my_file)
	next(my_file_reader)
	for data_row in my_file_reader:
		if "fighting" in data_row[1].lower():
			data_row.append("Combat")
			print data_row
		elif "fighting" not in data_row[1].lower():
			data_row.append("Other")
			print data_row
