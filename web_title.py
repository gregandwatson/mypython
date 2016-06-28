#!/usr/bin/python

import os
from urllib2 import urlopen

my_address = "https://realpython.com/practice/aphrodite.html" #setting variable to web address
html_page = urlopen(my_address) #setting variable to create fh 
html_text = html_page.read() #creates variable and uses read function to read html source

#print html_text

start_tag = "<title>"
end_tag = "</title>"

start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

print html_text[start_index:end_index]
print start_index
print html_text.find(start_tag)
print html_text.find(end_tag)
