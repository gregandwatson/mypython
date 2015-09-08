#!/usr/bin/python

import os
from pyPdf import PdfFileReader

my_path = "/root/chapter10/book1-exercises/Course materials/Chapter 12/Practice files" #set path to documents

input_file_name = os.path.join(my_path, "Pride and Prejudice.pdf") #joining path to actual file name to create file handle

input_file = PdfFileReader(file(input_file_name, "rb")) #created file object

print "Number of pages:", input_file.getNumPages() #used method to get number of pages in file object

print "Title:", input_file.getDocumentInfo().title # used method to get title of document from file object

print input_file.getPage(1).extractText()
