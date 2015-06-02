#!/usr/bin/python

enrollment = [['California Institute of Technology', 2175, 37704], ['Harvard', 19627, 39849], [ 'Massachusetts Institute of Technology' , 10566 , 40732 ], [ 'Princeton' , 7802 , 37000 ], [ 'Rice' , 5879 , 35551 ], [ 'Stanford' , 19535 , 40569 ], [ 'Yale' , 11701 , 40500 ]]

student = []
tuition = []
def enrollment_stats(enrollment):
	all_tuition = 0
	for i in enrollment:
		student.append(i[1])
		tuition.append(i[2])
#	print student
#	print tuition
	for total_tuition in tuition:
		all_tuition += total_tuition
#	print all_tuition

def mean(student):
	total_enrolled = 0
	for total in student:
		total_enrolled += total
#	print total_enrolled
	mean_of_list = total_enrolled / len(student)
#	print mean_of_list

def median(tuition):
	tuition.sort()
#	print tuition[3]

enrollment_stats(enrollment)
mean(student)
median(tuition)

print "*****************************************"
#print "Total students: ", total_enrolled
print "Total tuition: ", all_tuition
print ""
print ""
print "Student mean: ", mean_of_list
print "Student median: ", tuition
