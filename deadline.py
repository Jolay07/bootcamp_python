import datetime


""""Countdown app"""

# python:17.03.2023
print(datetime.datetime)
user_input = input("Enter your goal, sepereted by colon: course_name: dd.mm.yyyy: ")
course = user_input.split(':')

deadline1 = course[1]

deadline = datetime.datetime.strptime(deadline1, "%d.%m.%y")
calculation = deadline - int(datetime.datetime.now())
print(calculation)