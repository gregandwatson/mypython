#!/usr/bin/python

import urllib
from BeautifulSoup import *
import re
url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
print tags
for tag in tags:
	print tag.get('href', None)
