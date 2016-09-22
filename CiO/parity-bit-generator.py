def checkio(message):
    message = filter(lambda b: not bin(b).count('1') & 1, message)
    return ''.join(chr(c>>1) for c in message)
