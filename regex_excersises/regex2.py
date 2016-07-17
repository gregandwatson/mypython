#!/usr/bin/python
import re

x = "This is 12 days of 4 weeks where I only live to see 354 stars"
y = re.findall ('[0-9]+', x)
z = re.findall ('[AEIOUaeiou]+', x)
print y
print z

s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2pm'
lst = re.findall('\S+@\S+', s)
print lst
