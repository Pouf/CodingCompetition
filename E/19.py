# Problem 19 - Counting Sundays
# You are given the following information, but you may prefer to do some 
# research for yourself.
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a 
# century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century 
# (1 Jan 1901 to 31 Dec 2000)?
import datetime
start = datetime.datetime(1901,1,1)
end = datetime.datetime(2000,12,31)
numweeks = (end-start).days
count = 0
for n in range(numweeks):
    d = start + datetime.timedelta(days=n)
    if d.day == 1 and d.weekday() == 6:
        count += 1
print(count)
dates_list = [if (start + datetime.timedelta(days=7*x)).day == 1]
print(dates_list)
