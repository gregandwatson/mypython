#!/usr/bin/python

import urllib
web_page = raw_input('Enter in the url: ')
fhand = urllib.urlopen(web_page)

for line in fhand:
	print line.strip()
