"""The title of the next 3 days is "Learn the basics of datetime and date\" """
import datetime

my_birthday = datetime.date(2000, 3, 16)  # year month day

print(my_birthday.day)  # access the day
print(my_birthday.month)  # access the month
print(my_birthday.year)  # access the year

td_negative = datetime.timedelta(-29)  # negative number will decrease the date
td_positive = datetime.timedelta(31)  # positive number will decrease the date

"""documentation: https://docs.python.org/3/library/datetime.html?highlight=date%20format"""
message = "My Birthday is on : {:%d of %B, %Y}"
print(message.format(my_birthday))

"""Different objects"""
date_object = datetime.date(1996, 4, 15)
time_object = datetime.time(20, 25, 9)
date_time_object = datetime.datetime(1998, 4, 1, 20, 26, 18)

"""access the current date"""
now = datetime.datetime.today()
print(now)

"""convert strings to datetime"""
first_day_school = "1/9/2006 08:00:00"
str_datetime_object = datetime.datetime.strptime(first_day_school, "%d/%m/%Y %H:%M:%S")
print(str_datetime_object)
