#!/usr/bin/python

import os
my_path = "/root/python_programs/practice_files"
my_output_file = os.path.join(my_path, "hello.txt")
written_file = open(my_output_file, "w")
lines_to_write = ["This is my file", "\n There are many like it, ", "\nbut this is mine."]
next_line = ["\nNON SEQUITIR"]
written_file.writelines(lines_to_write)
written_file.close()
