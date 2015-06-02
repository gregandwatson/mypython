#!/usr/bin/python

word = raw_input("Enter in a word: ")
if len(word) < 5:
	print "The word you entered was ", word , "and it is less than 5"
elif len(word) > 5:
	print "The word you entered was", word , "and it is greater than 5"
else:
	print "The word is equal to 5"
