#!/usr/bin/python

import os
import glob

my_path = "/root/images"
file_name = os.path.join(my_path, "*.jpg")
for full_path in glob.glob(file_name):
	file_size = os.path.getsize(full_path)
	if file_size > 2000:
		print full_path, file_size
