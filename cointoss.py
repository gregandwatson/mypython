#!/usr/bin/python
from __future__ import division
from random import randint


for trials in range (0, 10000):
	flips = 1
	coin_toss = randint(0,1)
	while coin_toss != randint(0,1):
		flips +=1
print "average = {} ".format(flips/10000 * 100)
