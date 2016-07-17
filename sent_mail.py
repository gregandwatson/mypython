#!/usr/bin/python

name = raw_input("Enter file name: ")
if len(name) < 1: 
	name = "mbox-short.txt"
words = {}
sent_list =list()
handle = open(name)
for line in handle:
	if not line.startswith('From '):continue
	line = line.rstrip()
	words = line.split()
	sent_list.append(words[1]) 
#print sent_list
counts = {}
for word in sent_list:
	counts[word] = counts.get(word, 0) + 1
#print counts

bigCount = None
bigWord = None
for sent,count in counts.items():
	if bigCount is None or count > bigCount:
		bigWord = sent
		bigCount = count
print bigWord, bigCount 
