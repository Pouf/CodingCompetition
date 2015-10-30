from datetime import date

def checkio(from_date, to_date):
    start = from_date.toordinal()
    A = from_date.weekday()
    end = to_date.toordinal()
    B = to_date.weekday()

    restdays = ((end-start) // 7) * 2

    if B < A or B == 6:
        restdays += 2
    elif B == 5:
        restdays += 1
    if not (end-start) % 7 and A == 6:
        restdays -= 1

    return restdays
