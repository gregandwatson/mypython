#!/usr/bin/python

tries = 0

while tries < 3:
	password = raw_input("Enter your password: ")
	if password == "Gambitl0gan777":
		break
	else:
		tries +=1
else:
	print "Suspicious activity. The authorities have been alerted."
