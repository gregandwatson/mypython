#!/usr/bin/python

import urllib
from BeautifulSoup import *
import re

numbers = []
url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
print tags
for tag in tags:
	print tag
	new_number = re.findall('\S+', tag)
	print new_number
 
