def checkio(str_number, radix):
    try:
        return int(str_number, base=radix)
    except:
        return -1
