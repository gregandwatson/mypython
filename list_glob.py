#!/usr/bin/python

import os
import glob

my_path = "/root/images"
png_files = os.path.join(my_path, "*png")

for file_name in glob.glob(png_files):
	new_file_name = file_name[0:len(file_name)-4] + ".jpg"
	os.rename(file_name, new_file_name)
	print new_file_name
