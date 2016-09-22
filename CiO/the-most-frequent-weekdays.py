from calendar import Calendar, day_name
from collections import Counter

def most_frequent_days(year):
    days = Calendar().yeardays2calendar(year)
    for i in range(3):
        days = sum(days, [])
    c = Counter(d[1] for d in days if d[0])
    return [day_name[d] for d in c if c[d] == max(c.values())]
