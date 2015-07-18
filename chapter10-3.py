#!/usr/bin/python
with open("poem.txt", "r") as fh_input:
	with open("output.txt", "w") as fh_output:

		for lines in fh_input.readlines():
			fh_output.writelines(lines)
