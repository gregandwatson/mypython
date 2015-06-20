#!/usr/bin/python

my_output_file = open("hello.txt", "w")
lines_to_write = ["This is my file", "\n There are many like it, ", "\nbut this is mine."]
next_line = ["\nNON SEQUITIR"]
my_output_file.writelines(lines_to_write)
my_output_file.close()
