#!/usr/bin/python
from __future__ import division
from random import random
win = 0
for tries in range(0, 10000):
	A = 0
	if random() >= .87:
		A +=1
	if random() >= .65:
		A +=1
	if random() >= .17:
		A +=1
	if A > 1:
		win +=1
	print win	
print "win percentage is ", win / 10000 * 100
print 5 / 2
