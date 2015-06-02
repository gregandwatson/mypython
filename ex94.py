#!/usr/bin/python
dictlist = dict()
lst = list()
bigcount = None
bigword = None
name = raw_input("Enter a file name: ")
fh =  open(name)
for line in fh:
	if not line.startswith('From '): continue
	email = line.split()
	lst.append(email[1])
for name in lst:
        dictlist[name] = dictlist.get(name,0) + 1
for word,count in dictlist.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print bigword,bigcount
