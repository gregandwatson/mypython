#!/usr/bin/python
import os

my_path = "/home/ggreenlee/intro_python"
all_directories = os.listdir(my_path)
for file_name in all_directories:
	full_path = os.path.join(my_path, file_name)
if os.path.isdir(full_path):
	print full_path
