#!/usr/bin/python

birthdays = {}
birthdays["Luke Skywalker"] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'

if 'Yoda' not in birthdays:
	birthdays['Yoda'] = 'unknown'

if 'Darth Vader' not in birthdays:
	birthdays['Darth Vader'] = 'unknown'
print birthdays
del(birthdays['Darth Vader'])
print birthdays
