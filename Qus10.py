'''
Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
'''

from datetime import datetime
date_time=datetime.today()
print(date_time)

#format change
d1=date_time.strftime("%d-%m-%Y and %I:%M %p")
print(d1)

d2=date_time.strftime("%d-%m-%y and %I:%M %p" )
print(d2)
