#!/usr/bin/python

x = (1, 190, 284, 219, 3903, 93)
for iter in x:
	print iter 
print max(x)
(c, d) = ('Greg', 109)
print d
newdic = dict()
newdic['greg'] = 42
newdic['rob'] = 43
for name, age in newdic.items():
	print name, age
ages = newdic.items()
print ages
print sorted(ages)
print newdic
print newdic.items()
newerdic = newdic.items()
print newerdic
