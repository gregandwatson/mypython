#!/usr/bin/python
x = 1
while x ==1:
    try:
        no_of_hours = float(raw_input('Enter in the number of hours you worked: \n'))
        rate = float(raw_input('Enter in the rate of pay: \n'))
        x = x - 1
    except:
          print('You did not enter in a number, please try again\n')
def payroll(no_hours, rate):
    if no_of_hours <= 40:
        regular_pay = rate * no_of_hours
        overtime_pay = 0
    else:
        overtime_hours = no_of_hours - 40
        ot_pay = rate * 1.5
        overtime_pay = overtime_hours * ot_pay
        regular_pay = 40 * rate
    total_pay = regular_pay + overtime_pay
    print'Your total pay is',total_pay , 'dollars.'

payroll(no_of_hours, rate)

