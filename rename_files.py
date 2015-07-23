#!/usr/bin/python
import os
import glob

my_path = "/root" 
possible_files = os.path.join(my_path, "*.gif")
print possible_files
print glob.glob(possible_files)
for file_name in glob.glob(possible_files):
	print file_name
	print 'Converting "{0}" to JPG...'.format(file_name)
	full_file_name = os.path.join(my_path, file_name)
	print full_file_name
	new_file_name = full_file_name[0:len(full_file_name)-4] +".jpg"
	os.rename(full_file_name, new_file_name)
#print file_names_list
