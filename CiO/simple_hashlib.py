import hashlib


def checkio(s, algo):
    result = eval('hashlib.{}(s.encode()).hexdigest()'.format(algo))
    return result
