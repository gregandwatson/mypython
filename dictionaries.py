#!/usr/bin/python

counts = dict()
names = ['Greg', 'Rob', 'Kris', 'Doug', 'Tone', 'Tone', 'Tone', 'Greg', 'Rob']
for name in names:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1
print counts

counts = dict()
names = ['Greg', 'Rob', 'Kris', 'Doug', 'Tone', 'Tone', 'Tone', 'Greg', 'Rob']
for name in names:
	counts[name] = counts.get(name,0) + 1
print counts
