#!/usr/bin/python

import os
import csv

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 10/Practice files/Output"

with open(os.path.join(my_path, "movies.csv"), "wb") as my_file:
	my_file_writer = csv.writer(my_file)
	my_file_writer.writerow(["Movie", "Rating"])
	my_file_writer.writerow(["Rebel Without a Cause", "3"])
	my_file_writer.writerow(["Batman Begins", "5"])
	my_file_writer.writerow(["The Dark Knight", "5"])
