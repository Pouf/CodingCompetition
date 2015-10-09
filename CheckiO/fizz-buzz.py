def checkio(n):
    return ' '.join(['Fizz'*(not n%3), 'Buzz'*(not n%5)]).strip() or str(n)
