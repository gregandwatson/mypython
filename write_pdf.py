#!/usr/bin/python

import os
from pyPdf import PdfFileReader

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 12/Practice files"

input_file_name = os.path.join(my_path, "Pride and Prejudice.pdf")
input_file = PdfFileReader(file(input_file_name, "rb"))

output_file_name = os.path.join(my_path, "Output/Pride and Prejudice.txt")

output_file = open(output_file_name, "w")

title = input_file.getDocumentInfo().title #get the file title

total_pages = input_file.getNumPages() #get the total page count
output_file.write(title + "\n")
output_file.write("Number of pages: {}\n\n".format(total_pages))

for page_num in range(0, total_pages):
	text = input_file.getPage(page_num).extract.Text()
	text= text.replace(" ", "\n")
	outpu_file.write(text)

output_file.close()


