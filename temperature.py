#!/usr/bin/python

from __future__ import division
temp1=int(raw_input("Enter in the temperature in Farenheit: "))
temp2=int(raw_input("Enter in the temperature in Celsius: "))

def convert_to_celsius(temp1):
	celsius = (temp1 - 32) * (5/9)
	print temp1, "converted to Celsius is " ,celsius
	return celsius
def convert_to_farenheit(temp2):
	farenheit = temp2 * (9/5) + 32
	print temp2, "converted to Farenheit is ", farenheit
	return farenheit
convert_to_celsius(temp1)
convert_to_farenheit(temp2)
