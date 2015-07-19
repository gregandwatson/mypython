#!/usr/bin/python
import os

my_path ="/home/ggreenlee" 
file_names_list = os.listdir(my_path)
for file_name in file_names_list:
	if file_name.lower().endswith(".jpg"):
		print 'Converting "{}" to GIF...'.format(file_name)
		full_file_name = os.path.join(my_path, file_name)
		new_file_name = full_file_name[0:len(full_file_name)-4] +".gif"
		os.rename(full_file_name, new_file_name)
#print file_names_list
