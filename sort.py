#!/usr/bin/python

unsorted_list=[45, 23, 42, 1, 65, 82, 13, 5]
sorted_list = []

d = len(unsorted_list)
print d
for x in range(d):
	min_value = min(unsorted_list)
#	sorted_list.append(min_value)
	assigned_value = unsorted_list.index(min_value)
	print unsorted_list
	sorted_list.append(unsorted_list[assigned_value])
	unsorted_list.remove(unsorted_list[assigned_value])
print sorted_list 

			
#print unsorted_list
