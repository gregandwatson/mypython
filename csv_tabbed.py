#!/usr/bin/python

import os
import csv

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 10/Practice files"
my_file = open(os.path.join(my_path, "tabbed wonka.csv"), "rb")
my_file_reader = csv.reader(my_file, delimiter="\t")
next(my_file_reader)
for row in my_file_reader:
	print row


