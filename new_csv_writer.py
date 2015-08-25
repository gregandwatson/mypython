#!/usr/bin/python

import os
import csv

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 10/Practice files/Output"

with open(os.path.join(my_path, "categorized pastimes.csv"), "wb") as my_file:
	new_header = ['Name', 'Favorite Pastime', 'Type of Pastime']
	my_file_writer = csv.writer(my_file)
	my_file_writer.writerow(new_header)
	list_files = os.listdir(my_path)
	print list_files
