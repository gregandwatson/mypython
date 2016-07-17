#!/usr/bin/python

import socket #imports socket library module
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates socket handle
mysock.connect( ('www.py4inf.com', 80) ) #makes actual socket connection to server

mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n') #retrieves html page

while True:
	data = mysock.recv(512)
	if ( len(data) < 1) :
		break
	print data
mysock.close()
