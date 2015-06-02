#!/usr/bin/python

from random import randint
toss_total= 0
for throws in range(1,10000):
	die1 = randint(1,6)
	die2 = randint(1,6)
	toss = die1 + die2
	toss_total = toss + toss_total
	print toss_total
toss_average = toss_total / throws
print toss_average

