from calendar import Calendar

def checkio(year):
    return str(Calendar().yeardays2calendar(year)).count('13, 4')
