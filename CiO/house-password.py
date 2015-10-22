def checkio(p):
    return not(p.isdigit() + p.isalpha() + p.isupper() + p.islower() + (len(p)<10))
