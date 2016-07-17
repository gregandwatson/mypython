#!/usr/bin/python

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
#    print line
    new_list = line.split()
    print new_list
    for words in new_list:
        if words in lst: continue
        lst.append(words)
lst.sort()
print lst
