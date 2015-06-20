#!/usr/bin/python

my_input_file = open("hello.txt", "r")
input_file = my_input_file.readlines()
for lines in input_file:
	print lines,
my_input_file.close()
