#!/usr/bin/python

file_name = raw_input('Tye file name: ')
counts ={}
fh = open(file_name)
words = fh.read()
word_list = words.split()
for each_word in word_list:
	counts[each_word] = counts.get(each_word, 0) + 1
print counts	

