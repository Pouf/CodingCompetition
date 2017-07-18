# Given a start date with a known week day, your program must compute the day
# of the week at another date anytime in the same year.


from datetime import datetime
from calendar import day_name, month_name


days = list(day_name)
months = [m[:3] for m in month_name]

year = 2007 + int(input()) # 2008 is a leap year. Input is 1 if leap year, 0 otherwise
source_day_of_week, source_month, source_day_of_month = input().split()
source = datetime(year, months.index(source_month), int(source_day_of_month))

target_month, target_day_of_month = input().split()
target = datetime(year, months.index(target_month), int(target_day_of_month))
start = days.index(source_day_of_week)
delta = target - source
result = days[(start + delta.days) % 7]

print(result)