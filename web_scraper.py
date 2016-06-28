#!/usr/bin/python

import os
from urllib2 import urlopen

my_address = "https://realpython.com/practice/aphrodite.html"
html_page = urlopen(my_address)
html_text = html_page.read()

print html_text
