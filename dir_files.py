#!/usr/bin/python

import os

my_path = "/root/python_programs"

file_names_list = os.listdir(my_path)

for file_name in file_names_list:
	if file_name.lower().endswith(".txt"):
		print 'Converting', file_name, 'to text'
		

