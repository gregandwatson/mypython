#!/usr/bin/python

with open("poem.txt", "r")as open_poem:
	with open("output.txt", "w")as output_poem:

		for lines in open_poem.readlines():
			output_poem.writelines(lines)
additional_lines = "This is an additional line of text"
output_poem = open("output.txt", "a")
output_poem.writelines(additional_lines)


