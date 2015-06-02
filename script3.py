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
    for i in lst:
        numbers = i + float(numbers)
    global average_numbers
    average_numbers = numbers / len(lst)
    return average_numbers
    
def get_average(students):
    homework = students['homework']
    average(homework)
    homework_average = average_numbers * 0.1
    quizzes = students['quizzes']
    average(quizzes)
    quizzes_average = average_numbers * 0.3
    tests = students['tests']
    average(tests)
    tests_average = average_numbers * 0.6
    global final_average
    final_average = homework_average + quizzes_average + tests_average
    return final_average
    global score
    score = final_average
def get_letter_grade(score):
    if score >= 90:
        final_grade = "A"
        print final_grade
        return "A"
    elif score < 90 and score >= 80:
        final_grade = "B"
        print final_grade
        return "B"
    elif score < 80 and score >= 70:
        final_grade = "C"
        print final_grade
        return "C"
    elif score < 70 and score >= 60:
        final_grade = "D"
        print final_grade
        return "D"
    elif score < 60:
        final_grade = "F"
        print final_grade
        return "F"
    else:
        return "NULL"


def get_class_average(class_list):
    class_average = 0
    for i in class_list:
        get_average(i)
        class_average = float(final_average + class_average) / 3
    print class_average

get_class_average(['lloyd', 'alice', 'tyler'])
