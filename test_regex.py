#!/usr/bin/python

import re

x = '<span class="comments">97</span>'
parsed = re.findall('[0-9]+', x)
print parsed
