#!/usr/bin/python

your_word = raw_input('Enter your word:\n')
length = len(your_word) - 1

while length >= 0:
	print your_word[length]
	length = length - 1
