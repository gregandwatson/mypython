#!/usr/bin/python
x = 1
while x == 1:
    try:
	number = int(raw_input("Enter an integer: "))
        x = x - 1
    except ValueError:
	print "That was not an integer."
        
