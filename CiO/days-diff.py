def days_diff(date1, date2):
    
    def days(date):
        y, m, d = date
        correction = m <= 2
        y -= correction; m += 12*correction - 3
        return d + (153*m + 2)//5 + \
                    365*y + y//4 - y//100 + y//400
        
    return abs(days(date1) - days(date2))
