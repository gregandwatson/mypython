#!/usr/bin/python

import os

images_path = "/root/images"
all_images = os.listdir(images_path)
for file_names in all_images:
	full_path = os.path.join(images_path, file_names)
	print full_path
