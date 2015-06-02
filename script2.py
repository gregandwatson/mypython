#!/usr/bin/python

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(lst):
    numbers= 0
    global average_numbers
    for i in lst:
        numbers = i + float(numbers)
        average_numbers = numbers / len(lst)
    homework_average = average_numbers * 0.1
    print homework_average
    return average_numbers
    
def get_average(students):
    homework = students['homework']
    average(homework)
#    homework_average = average_numbers * 0.1
#    return homework_average
#    print homework_average
#    for i in students['quizzes']:
#        average(i)
#        quizzes_average = average * 0.3
#        return quizzes_average
#	print quizzes_average
#    for i in students['tests']:
#        tests_average = average * 0.6
#        return tests_average
#	print tests_average

get_average({
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
})
